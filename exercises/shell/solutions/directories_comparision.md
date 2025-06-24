## How to compare two directories in Linux?

You can use the 'diff' command with the '-r' flag to compare two direcotries recursively.



### Example:
'''bash
diff -r folder1/ folder2/

This command compares all the files and subdirectories inside 'folder1' and 'folder2'.
If both directories have identical contents, it retuns nothing.
If there are differences,it showss which files differ or are missing.
