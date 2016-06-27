def writeStringtoFile(fileName, string1):
    f = open(fileName, 'r+')
    f.read
    f.write(string1 * 3)
    f = open(fileName, 'r+')
    text = f.read()
    return text

print(writeStringtoFile('newdocument.txt', 'movie'))

def writeStringtoFile(fileName, string):
    f = open('fileName', 'w')
    f.write(string * 3)
    text = f
    f.close()
    #f = open('fileName')
    #text = f.read()
    #f.close()
    print (text)

writeStringtoFile('document.txt', 'movie')
