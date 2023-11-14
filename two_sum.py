#Develop a function that takes a list of numbers and a target sum, returning the indices of the two numbers that add up to the target sum.
def two_sum(list,target):
    for i in range (len(list)):
        for j in range (i+1, len(list)):
            if list[i]+list[j]==target:
                return i,j

myList=[2,3,4,5,6,2,3,4,10]
target = 13
print(two_sum(myList,target))