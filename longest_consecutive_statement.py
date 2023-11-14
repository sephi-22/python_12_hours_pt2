#Create a function that finds the length of the longest consecutive elements sequence in an unsorted list.
#Hint: Use a set to achieve O(n) complexity, eliminating the need to sort the list.
def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak

print(longest_consecutive([1,2,3,4,5,6,3,2,1,234,2,4,5,2,23,4,5,6,6,7,8,9,10,11,12,13,15,23]))