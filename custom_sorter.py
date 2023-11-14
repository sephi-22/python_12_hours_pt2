#Write a function that sorts a list of tuples based on the second value in each tuple.
#Hint: Use the sorted function with a custom key parameter.
def custom_sorter (list):
    sorted_list = sorted(list, key=lambda x: x[1])
    return sorted_list

my_list = [(3, 9), (1, 5), (2, 7), (4, 2), (5, 1)]

print(custom_sorter(my_list))