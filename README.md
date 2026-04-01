# Media / File sorter 

This is a simple python script I made to automate sorting photos / videos into sub folders organized by year created. 

The user specifies a source and target directory and chooses whether the files should be copied or moved. The program then scans all files
in the source directory, reads each file's creation date, automatically creates subfolders by year, and then moves or copies files into 
the appropriate year folder in the target directory. 

# How to use
1. Update the source and target directory paths in the script
2. Run the script: python main.py
3. Enter C to copy files into target or M to move files from source to target  
