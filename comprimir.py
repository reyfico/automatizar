from distutils import extension
from PIL import Image

import os

downloadsfolder = "/home/fx/Pictures/PRTG/"

if __name__ == "__main__":
    for filename in os.listdir(downloadsfolder):
        name, extension = os.path.splitext(downloadsfolder + filename)
        #print (filename)
        #print (name)
        #print (extension)
        if extension in [".jpg", ".png", ".jpeg"]:
            picture = Image.open(downloadsfolder + filename)
            picture.save(downloadsfolder + "comprimida_"+filename, optimize=True, quality=60)