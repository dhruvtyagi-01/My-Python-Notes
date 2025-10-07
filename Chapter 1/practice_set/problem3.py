import os


def print_directory_contents(dir_path):
    try:
        entries = os.listdir(dir_path)  # get list of names in the directory
        print(f"Contents of directory '{dir_path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"Error: Directory '{dir_path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{dir_path}' is not a directory.")
    except PermissionError:
        print(f"Error: Permission denied for '{dir_path}'.")
    except OSError as e:
        print(f"Some OS error occurred: {e}")


if __name__ == "__main__":
    directory = input("Enter the directory path: ")
    print_directory_contents(directory)
