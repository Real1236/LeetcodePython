# Q2: Western Bookstore
# You successfully got the Western experience you were promised, but now it's 2 weeks into the semester and you haven't gone to a single class. You go to the Western Bookstore which sells n different books. Since you're late, there's only one copy of each book available to buy. You realize you need to get your **** together so you decide to be keener and buy books such that the total number of pages you buy is maximized. You know the price and number of pages of each book.

# Your budget is at most x. What is the maximum number of pages you can buy?

# There are 0 <= n <= 1000 books.

# The budget is 0 <= b <= 10^5.

# The price and number of pages in each book is between 1 and 1000 inclusive.

# Example:

# Input: budget = 10, bookPrices = [4,8,5,3], bookPages = [5,8,12,1]

# If you buy book 1 and 3, it costs 4 + 5 = 9 and you get 5 + 12 = 17 pages. This gives you the maximum number of pages while remaining inside your budget.

# Note you can't buy books 2 and 3, since it costs 8 + 5 = 13, which is outside your budget of 10.

# You can't buy book 3 twice because you can only buy each book once.

# If you bought books 1 and 4, it costs 4 + 3 = 7 which is inside your budget, but you only get 5 + 1 = 6 pages, which is less than the maximum pages of 17.

def maxPages(budget, bookPrices, bookPages):
    # Initialize the dp array
    dp = [0] * (budget + 1)
    
    # Iterate over each book
    for i in range(len(bookPrices)):
        # Iterate over each possible budget from high to low
        for j in range(budget, bookPrices[i] - 1, -1):
            # Update the dp value for the current budget
            dp[j] = max(dp[j], dp[j - bookPrices[i]] + bookPages[i])
            
    return dp[budget]

budget = 10
bookPrices = [4,8,5,3]
bookPages = [5,8,12,1]
print(maxPages(budget, bookPrices, bookPages))  # Output: 17

budget = 5
bookPrices = [4,8,5,3]
bookPages = [5,8,12,1]
print(maxPages(budget, bookPrices, bookPages))

budget = 20
bookPrices = [4,8,5,3]
bookPages = [5,8,12,1]
print(maxPages(budget, bookPrices, bookPages))

# This function works by iterating over each book and for each book, it iterates over each possible budget from high to low. For each possible budget, it updates the maximum number of pages that can be bought by either not buying the current book (i.e., dp[j]) or buying the current book (i.e., dp[j - bookPrices[i]] + bookPages[i]). The time complexity of this solution is O(n×b), where n is the number of books and b is the budget. The space complexity is O(b), which is the space required for the dp array. This is because the dp array has a size of budget + 1