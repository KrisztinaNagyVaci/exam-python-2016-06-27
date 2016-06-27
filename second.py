# Create a function that takes a filename and a string as parameter,
# it should write the string to the file 3 times
# example: when called with "tree.txt" and "apple",
# it should write "appleappleapple" to the file "tree.txt".
# the function should not raise an error on any output problem, for example
# denied permission

def writeStringtoFile(fileName, string1):
    f = open(fileName, 'r+')
    f.read
    f.write(string1 * 3)
    f = open(fileName, 'r+')
    text = f.read()
    return text

print(writeStringtoFile('newdocument.txt', 'movie'))
