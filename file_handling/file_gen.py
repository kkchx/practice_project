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

    formats = ['jpg', 'txt', 'pdf', 'doc', 'xls']
    counters = [0,0,0,0,0]
    for _ in range(num_files):
        file_format = random.choice(formats) # Choose a random format
        create_random_file(directory, file_format)
        if file_format == "jpg":
            counters[0]+=1
        elif file_format == "txt":
            counters[1]+=1
        elif file_format == "pdf":
            counters[2]+=1
        elif file_format == "doc":
            counters[3]+=1
        elif file_format == "xls":
            counters[4]+=1

    for i in range(4):
        print(f"{counters[i]} {formats[i]} were created")
    print(f"Total {num_files} were created in {directory}")
# def total_count(jpg_count, txt_count, pdf_count, doc_count, xls_count):
#     total = jpg_count+txt_count+pdf_count+doc_count+xls_count
#     print(f"{jpg_count} jpg created")
#     print(f"{txt_count} txt created")
#     print(f"{pdf_count} pdf created")
#     print(f"{doc_count} doc created")
#     print(f"{xls_count} xls created")
#     print(f"Total {total} files created.")

if __name__ == "__main__":
    main()