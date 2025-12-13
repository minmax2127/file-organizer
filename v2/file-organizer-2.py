from pathlib import Path
import sys
import subprocess


def get_directory(arguments):
    if(len(arguments) != 2):
        print(f"Usage: {arguments[0]} [directory]")
        sys.exit(1)

    directory = arguments[1]
    try:
        directory = Path(directory)
        if(directory.is_dir()):
            return directory
        else:
            print("Not a directory!")
            return None
    except FileNotFoundError:
        print("Error!")

def organize_by_type(files, directory):
    extensions = []
    for f in files:
        # create directory
        dirpath = Path(str(directory) + "/" + str(f.suffix[1:]))
        try:
            dirpath.mkdir()
        except FileExistsError:
            print(f"{dirpath} already exists!")

        # add file to the directory
        filepath = Path(str(dirpath) + "/" + f.name)
        try:
            f.rename(filepath)
        except FileExistsError:
            print(f"{filepath} already exists!")
        except Exception:
            print(f"{filepath} cannot be saved!")
        
def show_tree(directory):
    # Example: Run 'ls -l'
    result = subprocess.run(['clear'])
    result = subprocess.run(['tree', str(directory)])

    # The returncode attribute indicates the command's exit status (0 usually means success)
    print(f"Command exited with return code: {result.returncode}")

def main():
    directory = get_directory(sys.argv)
    files = [entry for entry in directory.iterdir() if entry.is_file()]

    organize_by_type(files, directory)
    show_tree(directory)
    

if __name__ == "__main__":
    main()