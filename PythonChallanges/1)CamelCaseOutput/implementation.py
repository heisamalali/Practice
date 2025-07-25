import re

inputString = input('please enter a string')
listOfWords = []
outputString = ''
if inputString is None:
    raise Exception("Exception")
else:
    listOfWords = re.split('[ ,-]',inputString)

print(listOfWords)
def calculate_camel_case(list_of_words):
    output = ''
    for wordItem in list_of_words:
        print(wordItem)
        for index, char in enumerate(wordItem):
            if index == 0:
                output += char.upper()
            else:
                output += char.lower()
    return output

outputString += calculate_camel_case(listOfWords)



print(outputString)

