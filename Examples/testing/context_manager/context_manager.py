import os, random, shutil, time

class TemporaryDirectory(object):
    def __init__(self,directory):
        self.base_directory = directory

    def __enter__(self):
        # set things up
        self.directory = os.path.join(self.base_directory, str(random.random()))
        os.makedirs(self.directory)
        return self.directory

    def __exit__(self, type, value, traceback):
        # tear it down
        shutil.rmtree(self.directory)

with TemporaryDirectory("/tmp/foo") as dir:
    # write some temp data into dir
    with open(os.path.join(dir, "foo.txt"), 'w') as f:
        f.write("foo")

    time.sleep(5)
