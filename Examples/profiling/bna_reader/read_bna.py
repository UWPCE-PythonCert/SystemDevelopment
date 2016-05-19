#!/usr/bin/env python
"""
A module that contains a function for reading "BNA" format files
"""
import os
import numpy as np
import polygons

# try to import the filescanner It's a Cyton module for faster file reading
# but it only works with Python2 :-(
try:
    from filescanner import scan
    print("Using filescanner")
    FILESCANNER = True
except ImportError:
    print("Not using filescanner")
    FILESCANNER = False


class FileToolsException(Exception):
    '''
        The base class for all exceptions in the FileTools module
    '''
    pass


class BnaError(FileToolsException):
    pass


class BNAData:
    '''
        Class to store the full set of data in a BNA file
    '''
    # fixme: This needs methods to add polygons one by one
    def __init__(self, PointsData=None, Names=None, Types=None, Filename=None):
        '''
            :param PointsData: A sequence of numpy Nx2 arrays
                               of the points (x,y)
                               i.e. long,lat
            :param Names: A sequence of stings for the names of the polygons
            :param Types: A sequence of strings for the types of the polygons.
        '''
        self.PointsData = PointsData
        self.Filename = Filename
        self.Names = Names
        self.Types = Types

        try:
            l1 = len(PointsData)
        except TypeError:
            l1 = 0

        try:
            l2 = len(Names)
        except TypeError:
            l2 = 0

        try:
            l3 = len(Types)
        except TypeError:
            l3 = 0

        if l1 != l2 != l3:
            raise TypeError('PointsData, Types, and Names must be '
                            'the same length')

    def __getitem__(self, index):
        return (self.PointsData[index], self.Names[index])

    def __len__(self):
        return len(self.PointsData)

    def __str__(self):
        return 'BNAData instance: {0} polygons'.format(len(self))

    def save(self, filename=None):
        if not filename:
            filename = self.filename

        fd = open(filename, 'w')
        for i, points in enumerate(self.PointsData):
            fd.write('"%s","%s", %i\n' % (self.Names[i],
                                          self.Types[i],
                                          len(points)))
            for p in points:
                fd.write("%.12f,%.12f\n" % (tuple(p)))


def get_next_polygon(f, dtype=np.float64):
    """
    Utility function that returns the next polygon from a BNA file

    returns: (points, poly_type, name, sname) where:
        points:    Nx2numpy array of floats with the points
        poly_type: one of "point", "line", "poly"
        name:      name defined in the BNA
        sname:     secondary name defined in the BNA

    NOTE: It is the BNA standard to duplicate the first and last points.
          In that case, the duplicated last point is removed.

           "holes" in polygons are not supported in this code.
    See:
       http://www.softwright.com/faq/support/boundary_file_bna_format.html

    NOTE: This code doesn't allow extra spaces around the commas in the
          header line.
          If there are no commas allowed in the name, it would be easier to
          simply split on the commas
          (or march through the line looking for the quotes -- regex?)
    """
    while True:  # skip blank lines
        header = f.readline()
        if not header:  # end of file
            return None
        if header.strip():  # found a header
            break
        else:
            continue
    try:
        fields = header.split('"')
        name = fields[1]
        sname = fields[3]
        num_points = int(fields[4].strip()[1:])
    except (ValueError, IndexError):
        raise ValueError('something wrong with header line: {0}'
                         .format(header))

    if num_points < 0 or num_points == 2:
        poly_type = 'polyline'
        num_points = abs(num_points)
    elif num_points == 1:
        poly_type = 'point'
    elif num_points > 2:
        poly_type = 'polygon'
    else:
        raise BnaError("polygon {0} does not have a valid number of points"
                       .format(name))

    if FILESCANNER:
            points = scan(f, num_points * 2)
            points = np.asarray(points, dtype=dtype)
            points.shape = (-1, 2)
    else:
        points = np.zeros((num_points, 2), dtype)
        for i in range(num_points):
            points[i, :] = [float(j) for j in f.readline().split(',')]

    if poly_type == 'polygon':  # first and last points are the same in BNA,
                                # but we don't want the duplicate point.
        if (points[0, 0] == points[-1, 0] and points[0, 1] == points[-1, 1]):
            points = points[0:-1]

    return (points, poly_type, name, sname)


def write_bna(filename, polyset):
    """
    Writes a BNA file to filename

    polyset must be a A geometry.polygons.PolygonSet object,
              with metadata- (poly_type, name, secondary name)
    (such as returned by ReadBNA)
    """
    outfile = open(filename, 'w')

    for poly in polyset:
        m = poly.metadata
        outfile.write('"%s","%s", %i\n' % (m[1], m[2], len(poly)))

        for point in poly:
            outfile.write('%.8f, %.8f \n' % (point[0], point[1]))


# @profile
def read_bna(filename, polytype="list", dtype=np.float64):
    """
    Read a bna file.

    :param filename: path of file to read.

    :param polytype: type of polygons to return. options are:
                     "list" or "PolygonSet"

    :param dtype: data type of coordinates
    :type dtype: numpy dtype object

    Results are returned as one of:
    - "list": A list of tuples:
              (points, poly_type, name, secondary name)

    - "PolygonSet": A geometry.polygons.PolygonSet object,
                    with metadata- (poly_type, name, secondary name)

    - "BNADataClass": A BNAData class object -- this may be broken now!

    The dtype parameter specifies what numpy data type you want the points
    data in -- it defaults to np.float (C double)
    """
    fd = open(filename, 'r')

    if polytype == 'list':
        output = []

        while True:
            poly = get_next_polygon(fd, dtype=dtype)
            if poly is None:
                break
            output.append(poly)
    elif polytype == 'PolygonSet':
        output = polygons.PolygonSet(dtype=dtype)

        while True:
            poly = get_next_polygon(fd)
            if poly is None:
                break
            # fixme: should this be a dict, instead?
            output.append(poly[0], poly[1:])

    elif polytype == 'BNADataClass':
        polys = polygons.PolygonSet()
        Types = []
        Names = []
        while 1:
            line = fd.readline()
            if not line:
                break

            line = line.strip()
            Name, line = line.split('","')
            Name = Name[1:]
            Type, line = line.split('",')
            num_points = int(line)
            Types.append(Type)
            Names.append(Name)
            polygon = np.zeros((num_points, 2), np.float)

            for i in range(num_points):
                polygon[i, :] = map(float, fd.readline().split(','))
            polys.append(polygon)

        output = BNAData(polys, Names, Types, os.path.abspath(filename))
    else:
        raise ValueError('polytype must be either "BNADataClass", "list" '
                         'or "PolygonSet"')

    fd.close()
    return output

if __name__ == "__main__":
    # a sample run
    polys = read_bna("ChesapeakeBay.bna", "PolygonSet")
    # polys = read_bna("small.bna", "PolygonSet")
    print(polys)

