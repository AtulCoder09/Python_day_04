f = open("file.txt")
print(f.read())
f.close()

# with statement is used to automatically close the file after the block of code is executed. It ensures that the file is properly closed, even if an error occurs within the block.    
with open("file.txt") as f:
    print(f.read()) 

# The with statement is used to automatically close the file after the block of code is executed. It ensures that the file is properly closed, even if an error occurs within the block.