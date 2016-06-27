def writeStringtoFile(fileName, string1):
    f = open('fileName', 'r+')
    text = f.write('string1')
    f.close()
    print (text)

writeStringtoFile('newdocument.txt', 'movie')


def writeStringtoFile(fileName, string1):
    f = open('fileName', 'r+')
    lines = f.read
    f.close()
    f.write(string1 * 3)
    f = open('fileName', 'r+')
    text = f.read()
    return text

print(writeStringtoFile('newdocument.txt', 'movie'))
