#
# @lc app=leetcode id=846 lang=python3
#
# [846] Hand of Straights
#

# @lc code=start
from collections import Counter
import heapq
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        if groupSize == 1:
            return True
        
        cards = Counter(hand)
        heap = list(cards.keys())
        heapq.heapify(heap)
        while heap:
            firstCard = heap[0]
            for card in range(firstCard, firstCard + groupSize):
                if card not in cards:
                    return False
                cards[card] -= 1
                if cards[card] == 0:
                    cards.pop(card)
                    heapq.heappop(heap)
        return True

# @lc code=end
solution = Solution()
print(solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3))
print(solution.isNStraightHand([1,2,3,4,5], 4))
