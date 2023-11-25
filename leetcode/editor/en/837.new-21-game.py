#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # Calculate probability of going over 'n' points

        # Initialize probability of going over 'n' points
        # index -> total pts; value -> probability of going over 'n' points
        ptsProb = [0 for _ in range(k + maxPts)]

        # Use dynamic programming to calculate probability of going over 'n' points more efficiently
        windowSum = 0

        # Iterate backwards since the probability of going over 'n' points for lower point totals
        # depends on the probability of going over 'n' points for higher point totals
        for totalPts in range(k + maxPts - 1, -1, -1):
            # If player goes over 'n' points, they're guaranteed to go over 'n' points
            # If player goes under 'n' points but greater than 'k' points, it's impossible to to go over 'n' points
            # If player goes under 'k' points, they have a chance of going over 'n' points
            if totalPts > n:
                ptsProb[totalPts] = 1
                windowSum += 1
            elif totalPts <= n and totalPts >= k:   
                ptsProb[totalPts] = 0
            else:
                # Calculate probability of going over 'n' points
                # by summing the probabilities of going over 'n' points for the next 'maxPts' points
                # and dividing by 'maxPts'
                windowSum += ptsProb[totalPts + 1]
                ptsProb[totalPts] = windowSum / maxPts
                windowSum -= ptsProb[totalPts + maxPts]
        
        # Answer is 1 - probability of going over 'n' points
        return 1 - ptsProb[0]

# @lc code=end
solution = Solution()
print(solution.new21Game(10, 1, 10))
print(solution.new21Game(6, 1, 10))
print(solution.new21Game(21, 17, 10))
