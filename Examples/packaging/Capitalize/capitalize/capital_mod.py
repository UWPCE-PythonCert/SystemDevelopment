#!/usr/bin/env python

"""
A really simple module, just to demonstrate packaging
"""

def capitalize_line(instr):
    """
    capitalizes the input string 

    :param instr: the string to capitalize it should be a single line.
    :type instr: string

    :returns: a capitalized version of instr
    """

    return " ".join( word.capitalize() for word in instr.split() )


def capitalize(infilename, outfilename):
    """
    reads the contents of infilename, and writes it to outfilename, but with
    every word capitalized

    note: very primitive -- it will mess some files up!

    this is called by the capitalize script

    :param infilename: The file name you want to process
    :type infilename: string

    :param outfilename: the name of the new file that will be created
    :type outfilename: string
    
    :returns: None

    :raises: IOError if infilename doesn't exist.
    """
    infile = open(infilename, 'U')
    outfile = open(outfilename, 'w')

    for line in infile:
        outfile.write(capitalize_line(line))
        outfile.write("\n")
    
    return None