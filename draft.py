def writeStringtoFile(fileName, string):
    f = open('fileName', 'w')
    f.write(string * 3)
    text = f
    f.close()
    f = open('fileName')
    text = f.read()
    f.close()
    return text

print(writeStringtoFile('document.txt', 'movie'))
