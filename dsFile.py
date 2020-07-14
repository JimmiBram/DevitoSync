import os, hashlib

class dsFile:
    def __init__(self, path, new_base_path = ""):
        self.path = path
        self.md5 = ""
        self.basepath = new_base_path
    
    # def __hash__(self) -> str:
    #     return self.md5

    def get_relative_path(self) -> str:
            return self.path.replace(self.basepath, '')