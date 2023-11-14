#Write a function that uses regular expressions to check if a given string matches a given patttern
import re

def is_match (s,pattern):
    regex = re.compile(pattern)
    return regex.fullmatch(s) is not None

myString="bob-222@gmail.com"
input_pattern = r"^\w+@(\w+\.)?\w+\.\w+$"

print(is_match(myString,input_pattern))