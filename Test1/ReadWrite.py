file = open("test.txt")
# read all the contents of the file
# if want to read a certain amount of letter do file.read(2) for 2 characters
#print(file.read())

#readline method
#for line in file.readline():
#   print(file.readline())

#readlines method
#this method will read the context line by line (single line at a time)
for line in file.readlines():
    print(line)
# OR
#line = file.readline()
#while line != "blank":
#   print(line)
#   line = file.readline()

# whenever open file make sure to close the file. To avoid memory leaks
file.close()