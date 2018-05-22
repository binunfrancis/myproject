import os
import os.path

GIT_URL = "https://github.com/renjithcg/MyProjects.git"
PATH = "/home/server"


os.chdir(PATH)
os.system("git clone %s" % GIT_URL)








