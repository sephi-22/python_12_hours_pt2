#Create a function that checks whether two strings are anagrams of each other.
def anagram_checker (str1,str2):
    dict1={}
    dict2={}
    for i in str1.lower().replace(" ",""):
        dict1[i]=str1.lower().count(i)
    for j in str2.lower().replace(" ",""):
        dict2[j]=str2.lower().count(j)
    return dict1==dict2

#Better implementation
def anagram_checker2 (str1,str2):
    str1 = str1.lower().replace(" ","")
    str2 = str2.lower().replace(" ","")
    return sorted(str1)==sorted(str2)


print(anagram_checker("vacation time", "i am not active"))
print(anagram_checker("arrda","radar"))
print(anagram_checker2("debit card","bad credit"))
print(anagram_checker2("Eleven plus two","twelve plus one"))
