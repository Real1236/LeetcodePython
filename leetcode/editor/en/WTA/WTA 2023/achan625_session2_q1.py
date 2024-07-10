# Question 1
# Staples has a printer cartridge recycling program. For every cartridge recycled, the customer has two options: 
# Option 1: Earn a certain number of dollars for each cartridge.
# Option 2: Combine the cartridge with a certain number of dollars in order to purchase special "perk products"
# A customer is currently enrolled in this program and would like to purchase the maximum number of perk products. Given a certain number of cartridges and dollars, and how many perk products can the customer buy? 

# Example: 
# Input:
# cartridges = 10
# dollars = 10
# recycleReward = 2, the amount earned by recycling a single cartridge 
# perksCost = 2 the amount required for a customer to buy a single perk product combined with a recycled cartridge. 
# Output:
# 7
# Explanation: 
# The customer can first recycle 3 cartridges, earning 6 dollars. After this, 7 cartridges and 16 dollars left. The 7 cartridges can be combined with 14 dollars to purchase 14 dollars to purchase 7 perk items. 

# Example: 
# Input:
# cartridges = 4
# dollars = 8
# recycleReward = 3, the amount earned by recycling a single cartridge 
# perksCost = 4, the amount required for a customer to buy a single perk product combined with a recycled cartridge. 
# Output:
# 2
# Explanation: 
# The customer can combine cartridges with 8 dollars to buy 2 perk products. 


class Solution:
    def maxPerkProducts(self, cartridges: int, dollars: int, recycleReward: int, perksCost: int) -> int:
        curMax = min(dollars // perksCost, cartridges)
        nextMax = min((dollars + recycleReward) // perksCost, cartridges - 1)

        while curMax < nextMax:
            dollars += recycleReward
            cartridges -= 1

            curMax = nextMax
            nextMax = min((dollars + recycleReward) // perksCost, cartridges - 1)
        
        return max(curMax, nextMax)

solution = Solution()    

# Example 1
print(solution.maxPerkProducts(10, 10, 2, 2))

# Example 2
print(solution.maxPerkProducts(4, 8, 3, 4))

# Test Case 1 - 0 cartridges
print(solution.maxPerkProducts(0, 8, 3, 4))

# Test Case 2 - 1 cartridge
print(solution.maxPerkProducts(1, 10, 2, 2))

