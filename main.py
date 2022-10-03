from distutils import extension
from pickletools import optimize
from PIL import Image
import os

downloadFolder = "/Users/maino/Downloads/"

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadFolder + filename)
            picture.save(downloadFolder + "compressed_"+filename, optimize=True,quality=60)
