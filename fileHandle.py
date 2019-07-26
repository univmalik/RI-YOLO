import glob

# files_L = glob.glob("C:/Users/Administrator/PycharmProjects/openCV/img/*.txt")

# get python list of files either with .txt or .jpg
def files_LTXT(pathF):
    return glob.glob(pathF + "/*" + ".txt")

def files_LJPG(pathF):
    return glob.glob(pathF + "/*" + ".jpg")
