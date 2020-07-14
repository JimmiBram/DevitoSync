import os, shutil
from dsFile import dsFile
from dsDirectory import dsDirectory

from utils import io

fromdir_path = r'C:\temp\fromdir'
todir_path = r'C:\temp\todir'

#sync(path, copyto, 'sync', verbose=True, ctime=True)

def main():
    
    fd = dsDirectory(fromdir_path)
    fd.update()

    fd.print()
    io.write_json("c:\\temp\\folder.json", fd)
    

if __name__ == "__main__":
    main()