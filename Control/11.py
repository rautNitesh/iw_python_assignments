# Create a variable, filename. Assuming that it has a three-letter
# extension, and using slice operations, find the extension. For
# README.txt, the extension should be txt. Write code using slice
# operations that will give the name without the extension. Does your
# code work on filenames of arbitrary length?
# This works on any length of the file name but only on the extension with 3 letters.
#The uncommented way works for only if the file name doesn't have dot in it beside the extension


def getExtension(name):
    l=name.split(".")
    # return name[-3:len(name)]
    return l[1]

def getFilename(name):
    l=name.split(".")
    # return name[:-4]
    return l[0]


name="Readme.jpeg"
print(f"Extension :{getExtension(name)}")
print(f"Filename :{getFilename(name)}")