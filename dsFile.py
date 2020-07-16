from __future__ import annotations #<-- Makes sure the fromlist method can return a dsFile object. Redundant in Python 4
import os, hashlib


class dsFile:
    def __init__(self, path, new_base_path = ""):
        self.path = path
        self.md5 = ""
        self.basepath = new_base_path
    
    def __hash__(self) -> str:
        return self.md5

    def get_relative_path(self) -> str:
            return self.path.replace(self.basepath, '')

    def to_list(self) -> list:
        return [self.path, self.basepath, self.md5]

    @staticmethod
    def from_list(data: list) -> dsFile:
        return_object = dsFile(data[0], data[1])
        return_object.md = data[3]
        return return_object