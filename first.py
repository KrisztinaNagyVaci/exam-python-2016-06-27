# Create a function that takes a list as a parameter,
# and returns a new list with every second element from the orignal list
# It should raise an error if the parameter is not a list
# example: [1, 2, 3, 4, 5] should produce [2, 4]

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
