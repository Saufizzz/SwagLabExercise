# whenever you open any files make sure you close that file to avoid memory leaks due to open multiple files



file = open("test.txt") #if its in different location need to enter full path into the parentheses
#read all the context of the file
#print(file.read(10)) # it reads n num of byte of text file / n num of characters
# readline and should not be used together because it will run after each arguments
print(file.readline())
file.close()

#print line by line using readline method
