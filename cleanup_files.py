import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    try:
        os.chdir('Lyrics/Lyrics')
    except:
        pass
    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))
    os.mkdir('temp')
    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))
        os.rename(filename, new_name)
        shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    pos = [i for i, e in enumerate(filename) if e.isupper() and filename[i - 1].islower()]
    blank = []
    for j in range(len(pos)):
        blank.append(filename[pos[j]:pos[j + 1]])
        blank.append(filename[pos[j]:])
    filename = " ".join(blank)
    filename = filename.title()
    filename = filename.split(".")
    filename[1] = filename[1].lower()

    new_name = ".".join(filename)
    new_name.replace(" ", "_")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))
        for filename in filenames:
            print(os.path.join(directory_name, filename))
            new_name = get_fixed_filename(filename)
            os.rename(os.path.join(directory_name, filename), os.path.join(directory_name, new_name))


main()
# demo_walk()
