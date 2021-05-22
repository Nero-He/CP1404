import os
import shutil


def main():
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue
        extent = filename.split('.')[-1]
        os.mkdir(extent)
        print("{}/{}".format(extent, filename))
        shutil.move(filename, '{}/'.format(extent) + filename)
