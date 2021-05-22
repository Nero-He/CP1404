import os


def main():
    # set a dictionary to carry out
    type_extent = {}
    try:
        os.chdir("FilesToSort")
    except FileNotFoundError:
        pass
    # get the list of the files in the dir
    for filename in os.listdir('FilesToSort'):
        extent = filename.split('.')[-1]
        if extent not in type_extent:
            category = input("What category would you like to sort doc files into? {}".format(extent))
            type_extent[extent] = category
            os.mkdir(category)
            os.rename(filename, "{}/{}".format(type_extent[extent], filename))


main()
