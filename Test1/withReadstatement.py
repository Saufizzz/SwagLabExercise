# using with statement it will open the file and once whole execution has completed it will close
# no need to use .close method.
# "r" is for read only and "w" if for write


#assg 1 read the file and store all line in list
# reverse the list
# write the list back to the file

with open("test.txt", "r") as reader:
    content = reader.readlines() # store the initial list
    reversed(content)  # reverse the initial list
    with open("test.txt", "w") as writer:
        for line in reversed(content):
            writer.write(line)


