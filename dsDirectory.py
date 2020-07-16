from __future__ import annotations #<-- Makes sure the fromlist method can return a dsDirectory object. Redundant in Python 4
import os, datetime, json
from dsFile import dsFile

class dsDirectory:
    def __init__(self, path = "", new_base_path = ""):
        self.path = path
        self.files = []
        self.subdirs = []
        self.basepath = path
        self.last_updated = '1900-01-01'
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

        self.last_updated = datetime.date.today()

    def to_dictionary(self) -> dict:
        container = {}
        container['path'] = self.path
        container['basepath'] = self.basepath
        container['last_updated'] = self.last_updated
        filelist = []
        subdirlist = []
        for f in self.files:
            filelist.append(f.to_list)
        
        for d in self.subdirs:
            subdirlist.append(d.serialize())

        container['files'] = filelist
        container['subdirs'] = subdirlist
        return container
    
    @staticmethod
    def from_dictionary(data: dict) -> dsDirectory:
        return_object = dsDirectory(data['path'], data['basepath'])
        return_object.last_updated = data['last_updated']
        for f in data["files"]:
            return_object.files.append(dsFile.from_list(f))

        for d in data['subdirs']:
            return_object.subdirs.append(dsDirectory.from_dictionary(d))

        return return_object

    def serialize(self) -> str:
        return_dict = self.to_dictionary()
        return json.dumps(return_dict)