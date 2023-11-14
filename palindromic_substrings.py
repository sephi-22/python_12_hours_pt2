#Write a function that finds and returns all the palindromic substrings of a given string.
#Hint: Consider using a sliding window technique to generate all possible substrings
def is_palindrome(s):
    return s.lower()==s.lower()[::-1]

def palindromic_substrings(string):
    palindrome_set = set()
    for i in range(len(string)):
        for j in range(i+1,len(string)+1):
            if is_palindrome(string[i:j]):
                palindrome_set.add(string[i:j])
    return list(palindrome_set)

print(palindromic_substrings("radarisjustaradarbutanapple is not an apple haha"))

