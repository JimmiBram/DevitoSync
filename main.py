import os, shutil
#from dirsync import sync

path = r'C:\temp\fromdir'
copyto = r'C:\temp\todir'

#sync(path, copyto, 'sync', verbose=True, ctime=True)

def main():
    index_dir(path)

def index_dir(path) -> list:
    files=os.listdir(path)
    files.sort()

    for f in files:
        src = path+'\\'+f
        if os.path.isfile(src) == True:
            print("Fil: %s [%s]" % (src, os.stat(src).st_mtime))
        else:
            print("Dir: %s" % src)


if __name__ == "__main__":
    main()