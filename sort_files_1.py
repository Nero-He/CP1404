import os
import shutil


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('FilesToSort'):
        extent = filename.split('.')[-1]
        os.mkdir(extent)
        print("{}/{}".format(extent, filename))
        shutil.move(filename, '{}/'.format(extent) + filename)
