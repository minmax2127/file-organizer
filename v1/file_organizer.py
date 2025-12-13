from pathlib import Path, PurePosixPath
import sys

'''
Program
- Get path
- Inside the path,
    - Get all files
    - Create directories: [Images, Videos, Codes, Text Files, Audio]
    - Move the files to their corresponding directory
'''

def get_path(arg_index):
    # get directory from the command-line argument
    if len(sys.argv) != arg_index + 1:
        print(f"Usage: python3 {sys.argv[0]} [directory-path]")
    else:
        directory = sys.argv[arg_index]
        
        # get correct directory name
        relative_path = Path(directory)
        path = relative_path.resolve()

        # check if the directory exists
        if path.is_dir():
            return path
        else:
            print(f"{path} does not exist!")

    sys.exit(0)

def create_directories(path, dirlist):
    full_directory_path = []
    for dir in dirlist:
        new_dirpath = Path(f"{path}/{dir}")
        full_directory_path.append(new_dirpath)
        try:
            new_dirpath.mkdir()
            print(f"{dir} created!")
        except FileExistsError:
            pass
    return full_directory_path

def organize_directory(path):
    # create directories
    dirlist = ["Images", "Videos", "Codes", "Text Files", "Audio", "Others"]
    directories_by_type = create_directories(path, dirlist)

    # get all files
    files = [entry for entry in path.iterdir() if entry.is_file()]
    folders = [entry for entry in path.iterdir() if entry.is_dir()]
    
    # move all the files to their proper directory
    for file in files:
        if file.suffix == ".png" or file.suffix == ".jpg":
            file.rename(f"{directories_by_type[0]}/{file.name}")
        elif file.suffix == ".mp4":
            file.rename(f"{directories_by_type[1]}/{file.name}")
        elif file.suffix == ".py":
            file.rename(f"{directories_by_type[2]}/{file.name}")
        elif file.suffix == ".png" or file.suffix == ".jpg" or file.suffix == ".jpeg":
            file.rename(f"{directories_by_type[3]}/{file.name}")
        elif file.suffix == ".txt":
            file.rename(f"{directories_by_type[3]}/{file.name}")
        elif file.suffix == ".mp3":
            file.rename(f"{directories_by_type[4]}/{file.name}")
        else:
            file.rename(f"{directories_by_type[5]}/{file.name}")

    print(f"Successfully organized your directory!")

def main():
    # Get path
    path = get_path(1)
    print(f"Fixing {path}  ...")

    # Organize files from the path
    organize_directory(path)

if __name__ == "__main__":
    main()
    

    

