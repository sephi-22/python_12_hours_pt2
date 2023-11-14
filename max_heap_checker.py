#Write a function that checks if a given list of numbers represents a valid max heap.
def is_max_heap(list):
    size = len(list)
    for i in range(size):
        child_1 = 2*i+1
        child_2 = 2*i+2
        if child_1 < size and list[i]<list[child_1]:
            return False
        if child_2<size and list[i]<list[child_2]:
            return False
    return True


numbers = [9, 7, 6, 5, 4, 3, 10, 1]
print(is_max_heap(numbers))