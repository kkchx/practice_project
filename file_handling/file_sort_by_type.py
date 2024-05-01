import os
import shutil

def sort_files_by_type(directory):
    # Create a list of files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        # Extract the file extension
        ext = file.split('.')[-1]
        if ext == file: # This handles files without an extension
            ext = 'no_extension'

        # Create a subdirectory for the file type if it doesn't exist
        subdirectory = os.path.join(directory, ext)
        if not os.path.exists(subdirectory):
            os.makedirs(subdirectory)

        # Move the file to the appropriate subdirectory
        shutil.move(os.path.join(directory, file), os.path.join(subdirectory, file))
        print(f"Moved {file} to {subdirectory}/")
def main():
    directory = input("Enter the directory to sort files in: ")

    if not os.path.exists(directory):
        print("Directory doesn't exist.")
        return

    sort_files_by_type(directory)
    print("Files have been sorted by type.")


if __name__ == "__main__":
    main()