#Create a function that takes a string and capitalizes every other letter in the string
#Hint: Use slicing with step and string concatenation or a join operation.

def capitalize_every_other(string):
    return ''.join([char.upper() if index % 2 == 0 else char for index, char in enumerate(string)])

original_string = "hello world"
result = capitalize_every_other(original_string)
print(result)