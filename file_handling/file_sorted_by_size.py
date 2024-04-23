import os
import shutil

def sort_files_by_size(directory):
    # Subdirectories for sorted files
    subdir_small = os.path.join(directory, "less_than_300kb")
    subdir_medium = os.path.join(directory, "equal_to_301-700kb")
    subdir_large = os.path.join(directory, "more_than_701kb")

    # Create subdirectories if they do not exist
    if not os.path.exists(subdir_small):
        os.makedirs(subdir_small)
    if not os.path.exists(subdir_medium):
        os.makedirs(subdir_medium)
    if not os.path.exists(subdir_large):
        os.makedirs(subdir_large)

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # Move files to appropriate subdirectories based on size
    for file in files:
        file_path = os.path.join(directory, file)
        size = os.path.getsize(file_path)

        if size < 300 * 1024: # less than 300 KB
            shutil.move(file_path, os.path.join(subdir_small, file))
            print(f"Moved {file} to {subdir_small}")
        elif size <= 700 * 1024:
            shutil.move(file_path, os.path.join(subdir_medium, file))
            print(f"Moved {file} to {subdir_medium}")
        else: # more than 701 KB
            shutil.move(file_path, os.path.join(subdir_large, file))
            print(f"Moved {file} to {subdir_large}")

def main():
    directory = input("Enter the directory to sort files by size: ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    sort_files_by_size(directory)
    print("Files have been sorted by size.")

if __name__ == "__main__":
    main()