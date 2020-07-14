import os
from dsFile import dsFile

class dsDirectory:
    def __init__(self, path = "", new_base_path = ""):
        self.path = path
        self.files = []
        self.subdirs = []
        self.basepath = path
        if new_base_path != "":
            self.basepath = new_base_path

    def print(self, indent: str = ""):
        for fi in self.files:
            print("%s%s (%s) (%s)" % (indent, fi.path, fi.get_relative_path(), fi.basepath))

        for di in self.subdirs:
            new_indent = indent + "----"
            print("%s [%s]" % (new_indent, di.path))
            di.print(new_indent)

    def get_relative_path(self) -> str:
        return self.path.replace(self.basepath, '')

    def update(self):
        self.files = []
        self.subdirs = []
        files=os.listdir(self.path)
        files.sort()

        for f in files:
            c_path = self.path+'\\'+f

            if os.path.isfile(c_path) == True:
                newfile = dsFile(c_path, self.basepath)
                newfile.basepath = self.basepath
                self.files.append(newfile)
            else:
                newsubdir = dsDirectory(c_path, self.basepath)
                newsubdir.update()
                self.subdirs.append(newsubdir)