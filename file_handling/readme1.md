## File Generator
This Python script generates random files of specified formats with random sizes and counts in a given directory.
Functionality

The script accomplishes the following tasks:
1. Prompts the user to enter a directory to create files in. 
2. Prompts the user to enter the number of files to create.
3. Ensures that the specified directory exists; if not, creates it.
4. Asks the user to input the file extensions (e.g., jpg, txt, doc) separated by commas. 
5. Creates random files with sizes ranging from 1KB to 1000KB in the specified directory.
6. Generates files with random names (a random integer followed by the file extension).
7. Outputs the count of files created for each specified format.
8. Prints the total number of files created in the specified directory.


## Usage
1. Run the script.<br>
2. Enter the directory path where you want to create the files.<br>
3. Specify the number of files you want to create.<br>
4. Input the file extensions separated by commas (e.g., jpg, txt, doc).<br>
5. The script will generate the files and display the count for each format as well as the total count of files created.


## Example
- Suppose you want to create 10 random files with extensions jpg, txt, and doc in the directory ./files.<br>
- bash<br>
- Enter the directory to create files in: ./files<br>
- Enter the number of files to create: 10<br>
- Enter the file extensions to create (separated by commas, eg., jpg, txt, doc): jpg, txt, doc

After running the script, you will see an output similar to the following:<br>
bash<br>
3 jpg were created<br>
3 txt were created<br>
4 doc were created<br>
Total 10 were created in ./files


### Note
- Make sure to provide a valid directory path.<br>
- Ensure you have necessary permissions to create files in the specified directory.<br>
- The script generates files with random content; use caution when creating large numbers of files.