## File Sorted By Extension
This script sorts files in a directory based on their types (extensions) into respective subdirectories.


## Example
Suppose you have a directory named `Documents` with various files: <br>
Documents/ <br>
├── resume.docx <br>
├── notes.txt <br>
├── image.jpg <br>
└── presentation.pptx

Running the script on this directory will result in:

Documents/ <br>
├── docx/ <br>
│ └── resume.docx <br>
├── txt/ <br>
│ └── notes.txt <br>
├── jpg/ <br>
│ └── image.jpg <br>
└── pptx/ <br>
└── presentation.pptx


## Requirements
- Python 3.x
- `os` module
- `shutil` module