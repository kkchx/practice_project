import os

def delete_files_by_extension(directory, extensions):
    normalized_extensions = {ext.strip().lower() for ext in extensions.split(",")}
    counters = {ext: 0 for ext in normalized_extensions}

    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    for file in files:
        file_ext = os.path.splitext(file)[1][1:].lower()
        if file_ext in normalized_extensions:
            os.remove(os.path.join(directory, file))
            counters[file_ext] += 1
    return counters

def main():
    directory = input("Enter the directory from which to delete files: ")
    extensions = input("Enter the file extensions to delete (separated by commas, eg., jpg, txt, doc): ")

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    counters = delete_files_by_extension(directory, extensions)
    for ext, count in counters.items():
        print(f"{count} {ext} were deleted.")

if __name__ == "__main__":
    main()
