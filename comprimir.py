from distutils import extension
from PIL import Image

import os

downloadsfolder = "/home/fx/Pictures/PRTG/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsfolder):
        name, extension = os.path.splitext(downloadsfolder + filename)
        print (filename)
        #print (name)
        print (extension)