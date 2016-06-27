def writeStringtoFile(fileName, string1):
    f = open('fileName', 'r+')
    f.write(string1)
    f.close()
    n = open('fileName')
    text = n.read()
    n.close()
    return text

print(writeStringtoFile('document.txt', 'movie'))
