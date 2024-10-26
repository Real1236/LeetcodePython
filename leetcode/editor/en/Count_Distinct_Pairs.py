# You are given an array of integers numbers. Your task is to count the number of distinct pairs (i, j) such that 0 ≤ i < j < numbers.length, and numbers[i] can be obtained from numbers[j] by swapping no more than two digits of numbers[j].

# Note: One may not need to swap any digits in the number at all, so if i < j and numbers[i] = numbers[j], the pair should also be counted.

# Example

# For numbers = [1, 23, 156, 1650, 651, 165, 32], the output should be solution(numbers) = 3.

# numbers[1] = 23 can be obtained from numbers[6] = 32 by swapping its only two digits.
# numbers[2] = 156 can be obtained from numbers[4] = 651 by swapping 6 and 1.
# numbers[2] = 156 can be obtained from numbers[5] = 165 by swapping 6 and 5.
# For numbers = [123, 321, 123], the output should be solution(numbers) = 3.

# All possible pairs should be counted:

# numbers[1] = 321 can be obtained from numbers[0] = 123 by swapping 1 and 3.
# numbers[2] = 123 can be obtained from numbers[0] = 123 by not swapping any digits at all.
# numbers[2] = 123 can be obtained from numbers[1] = 321 by swapping 3 and 1.
# Input/Output

# [execution time limit] 4 seconds (py3)

# [memory limit] 1 GB

# [input] array.integer numbers

# An array of positive integers.

# Guaranteed constraints:
# 1 ≤ numbers.length ≤ 104,
# 1 ≤ numbers[i] ≤ 109.

# [output] integer

# The count of pairs from numbers in which one number can be obtained by swapping two digits in the other number.