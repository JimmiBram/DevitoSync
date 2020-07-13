class dsDirectory:
    def __init__(self, path = ""):
        
        self.path = path
        self.files = []
        self.subdirs = []

    def add_file(self, newfile):
        self.files.append(newfile)

    def add_subdir(self, newsubdir):
        self.subdirs.append(newsubdir)