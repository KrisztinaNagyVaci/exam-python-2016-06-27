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

l = [1, 2, 3, 4, 5]
a = 'string'

def selectEverySecond(input):
    newList = []
    if isinstance(input, list):
        for item in input[1::2]:
            newList.append(item)
        return (newList)
    else:
        return 'The parameter is not a list'

print(selectEverySecond(l))

def refill(self):
    usedFuel = 0
    if self.rocket == 'falcon1':
        usedFuel = 5 - self.fuel
        self.fuel = 5
        return usedFuel
    if self.rocket == 'falcon9':
        originalFuel = self.fuel
        usedFuel = 20 - originalFuel
        self.fuel = 20
        return usedFuel
