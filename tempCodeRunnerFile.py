def longest_consecutive(nums):
    num_set = set(nums)
    longest_streak = 0
    print (num_set)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
                print("current num" + str(current_num) + "current streak" + str(current_streak))

            longest_streak = max(longest_streak, current_streak)

    return longest_streak