import os
def delete_files_by_extension(directory, extensions, counters):
    # Normalize the extensions to ensure consistency
    normalized_extensions = {ext.strip().lower() for ext in extensions.split(",")}

    # List all files in the directory
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    # Filter and delete files with the specified extensions
    for file in files:
        file_ext = os.path.splitext(file)[1][1:].lower() # Extract extension and convert to lowercase
        if file_ext in normalized_extensions:
            os.remove(os.path.join(directory, file))

def main():
    directory = input("Enter the directory from which to delete files: ")
    extensions = input("Enter the file extensions to delete (separated by commas, eg., jpg, txt, doc): ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    delete_files_by_extension(directory, extensions, counters)
    print("Requested files have been deleted.")

if __name__ == "__main__":
    main()