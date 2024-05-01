## File Sorted By Size
This script organizes files in a directory based on their sizes into subdirectories: less than 300 KB, medium (301-700 KB), and more than 701 KB.

## Example
Suppose you have a directory named `Files` with various files: 
Files/ <br>
├── document1.pdf (150 KB) <br>
├── document2.docx (600 KB) <br>
├── image1.jpg (250 KB) <br>
├── image2.png (800 KB) <br>
└── video.mp4 (1.5 MB) <br>

Running the script on this directory will result in:

Files/ <br>
├── less_than_300kb/ <br>
│ ├── document1.pdf <br>
│ └── image1.jpg<br> 
├── medium_301-700kb/<br>
│ └── document2.docx<br>
└── more_than_701kb/<br>
├── image2.png<br>
└── video.mp4


## Requirements
- Python 3.x
- `os` module
- `shutil` module