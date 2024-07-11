# Question 3
# There is a new alien language which uses the latin alphabet (a-z). However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Return the order of letters in this language.

# Note: Only one additional test case is required for this question.

# Example:
# Input: words = ["wrt", "wrf", "er", "ett", "rftt"]
# Output: "wertf"

# Explanation:
# From "wrt" and "wrf", we can get 't'<'f'
# From "wrt" and "er", we can get 'w'<'e'
# From "er" and "ett", we can get 'r'<'t'
# From "ett" and "rftt", we can get 'e'<'r'

# Example:
# Input: words = ["baa", "abcd", "abca", "cab", "cad"] 
# Output: "bdac"

# Explanation:
# From "baa" and "abcd" we get 'b' < 'a'
# From "abcd" and "abca" we get 'd' < 'a'
# From "abca" and "cab" we get 'a' < 'c'
# From "cab" and "cad" we get 'b' < 'd'

from collections import defaultdict
from typing import List


def getOrder(words: List[str]) -> str:
    # Build adjacency list
    adj = defaultdict(list)
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        for j in range(min(len(word1), len(word2))):
            char1, char2 = word1[j], word2[j]
            if char1 != char2:
                adj[char1].append(char2)
                break

    print(adj)

    def dfs(letter: str, visited: set, adj: map) -> str:
        if letter in visited:
            return ""
        visited.add(letter)

        if letter not in adj:
            return letter
        
        res = ""
        for next in adj[letter]:
            res += dfs(next, visited, adj)

        return res + letter

    return dfs(words[0][0], set(), adj)[::-1]

words = ["wrt", "wrf", "er", "ett", "rftt"]
print(getOrder(words))

words = ["baa", "abcd", "abca", "cab", "cad"]
print(getOrder(words))

words = ["caa", "aaa", "aab"]
print(getOrder(words))

# Iterated through the list, comparing 2 words at a time to build a directed-acyclic graph of the order of the alphabet. Then used topological sort to get the order of the alphabet. TC and SC are both O(n) because of DFS
