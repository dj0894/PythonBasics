
# Open a file, if not exist create one with write access

def main():

    f = open("testfile.txt", "w+")

# modyfing file
    for i in range(10):
        f.write("this is line "+str(i))

    f.close()


# # Opening file in append mode
    file = open("testfile.txt", "a+")

    file.write("this is appended line\n")
    file.close()

# # opening file to read file
    file = open("testfile.txt", "r")
    if file.mode == 'r':
        contents = file.read()
        print(contents)
    file.close()


main()
