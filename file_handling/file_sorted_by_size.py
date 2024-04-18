import os
import shutil

def sort_files_by_size(directory):
    print("Sorted goes here")

def main():
    directory = input("Enter the directory to sort files by size: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    sort_files_by_size(directory)
    print("Files have been sorted by size.")

if __name__ == "__main__":
    main()