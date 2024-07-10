# Question 1 - Sorting
# Given two arrays representing entry and exit times of guests at a party, find the time at which the maximum number of guests are present.
# Example 1:
# Input:
# entry = [1, 2, 9, 5, 5]
# exit = [4, 5, 12, 9, 12]
# Output:
# 5
# Explanation:
# The maximum number of guests (3) are present at time 5.
# Example 2:
# Input:
# entry = [3, 3, 9, 10, 8, 12]
# exit = [4, 6, 20, 15, 12, 16]
# Output:
# 12
# Explanation:
# The maximum number of guests (4) are present at time 12.

from typing import List


def time_max_guests(entry: List[int], exit: List[int]) -> int:
    entry.sort()
    exit.sort()
    
    entry_index, exit_index, res, max_count, count = 0, 0, 0, 0, 0
    while entry_index < len(entry) and exit_index < len(entry):
        if entry[entry_index] <= exit[exit_index]:
            count += 1
            if count > max_count:
                max_count = count
                res = entry[entry_index]
            entry_index += 1
        else:
            count -= 1
            exit_index += 1

    return res

entry = [1, 2, 9, 5, 5]
exit = [4, 5, 12, 9, 12]
print(time_max_guests(entry, exit))

entry = [3, 3, 9, 10, 8, 12]
exit = [4, 6, 20, 15, 12, 16]
print(time_max_guests(entry, exit))

# It sorts the lists and iterates through them simulatneously,  increasing a count whenever a guest enters and decreasing it when a guest leaves. The time at which the count is at its maximum is stored and returned as the result, indicating the peak time of attendance. TC is O(nlogn) for sorting the arrays.