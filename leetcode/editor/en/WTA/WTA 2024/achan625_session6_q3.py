# Q3: Perseverance
# University is way harder than high school. The LTC is always late, the local Potato Noodle spot closed down, and on top of it all, your prof has an awful grading scheme. For every bad assignment you submit, your prof subtracts one of the digits of your grade from your grade. Every assignment you submit is bad. You've had enough and decided you want a 0 in the course out of spite. What is the minimum number of assignments you need to submit so that your grade reaches 0?

# You are given your starting grade. Return the minimum number of assignments submitted such that your grade drops to 0.

# Your initial grade is an integer from 0 to 10^6.

# Example
# Input: 27
# Output: 5

# Your grade starts at 27. 

# After one assignment, your grade may drop to 27 - 7 = 20. (7 is a digit of 27).
# After the second, your grade may drop to 20 - 2 = 18 (2 is a digit of 20).
# The third, 18 - 8 = 10 (8 is a digit of 18)
# The fourth, 10 - 1 = 9 (1 is a digit of 10)
# The fifth, 9 - 9 = 0 (9 is a digit of 9)

# 27 -> 20 -> 18 -> 10 -> 9 -> 0

# It can be shown that the minimum number of assignments needed to reach 0 is 5. For example, after the first assignment, it is possible that your grade drops to 27 - 2 = 25 (2 is a digit of 27), but this would result in more assignments needed to reach a final grade of 0.

def minAssignments(grade):
    # Initialize the dp array
    dp = [0] + [float('inf')] * grade
    
    # Iterate over each possible grade
    for i in range(1, grade + 1):
        # Iterate over each digit of the current grade
        for digit in map(int, str(i)):
            # Update the dp value for the current grade
            dp[i] = min(dp[i], dp[i - digit] + 1)
            
    return dp[grade]

grade = 27
print(minAssignments(grade))

grade = 10
print(minAssignments(grade))

grade = 123
print(minAssignments(grade))

# This function works by iterating over each possible grade and for each grade, it iterates over each digit of the current grade. For each digit, it updates the minimum number of assignments needed to reach the current grade by either not subtracting the current digit (i.e., dp[i]) or subtracting the current digit (i.e., dp[i - digit] + 1). The time complexity of this solution is O(n×m), where n is the grade and m is the number of digits in the grade. The space complexity is O(n), which is the space required for the dp array. This is because the dp array has a size of grade + 1