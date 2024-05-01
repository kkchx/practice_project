import os
import random

def create_random_file(directory, file_format):
    # Create a file with random size between 1KB and 1000KB
    size = random.randint(1024, 1024000) # Size in bytes 1kb = 1024b and 1000kb = 1024000b
    filename = os.path.join(directory, f"{random.randint(1000, 9999)}.{file_format}")

    with open(filename, 'wb') as f:
        f.write(os.urandom(size)) # Write random bytes to file
def main():
    directory = input("Enter the directory to create files in: ")
    num_files = int(input("Enter the number of files to create: "))

    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)

    # formats = ['jpg', 'txt', 'pdf', 'doc', 'xls']
    extensions = input("Enter the file extensions to create (separated by commas, eg., jpg, txt, doc): ")
    formats = list({ext.strip().lower() for ext in extensions.split(",")})
    length_of_formats = len(formats)

    counters = []
    for item in formats:
        counters.append(0)

    for _ in range(num_files):
        file_format = random.choice(formats) # Choose a random format
        create_random_file(directory, file_format)
        for i in range(length_of_formats):
            if file_format == formats[i]:
                counters[i]+=1

    for i in range(length_of_formats):
        print(f"{counters[i]} {formats[i]} were created")
    print(f"Total {num_files} were created in {directory}")


if __name__ == "__main__":
    main()