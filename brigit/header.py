import os

def run_header(yelmox_version):

    ################################### Utilities ################################################
    # Set yelmox to current folder in order to run the shell commands correctly.
    path = "/p/projects/megarun/jan/yelmox/yelmox_"+yelmox_version
    def operateOnFolder(folder):
        os.chdir(path)

    for k in os.listdir("."):
        if os.path.isdir(k):
            operateOnFolder(k)
    return path