#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#

# @lc code=start
import heapq
from typing import List


class User:

    def __init__(self, userId: int):
        self.userId = userId
        self.followees = {}
        self.tweets = []
    
    def follow(self, followeeId: int, followee: 'User') -> None:
        self.followees[followeeId] = followee

    def postTweet(self, tweetId: int, time: int) -> None:
        self.tweets.append((time, tweetId))
    
    def unfollow(self, followeeId: int) -> 'User':
        if followeeId in self.followees:
            return self.followees.pop(followeeId)
    
    def getNewsFeed(self) -> List[int]:
        feed = []
        for user in self.followees.values():
            num_of_tweets = len(user.tweets)
            for i in range(num_of_tweets - 1, max(-1, num_of_tweets - 11), -1):
                feed.append(user.tweets[i])
                
        num_of_tweets = len(self.tweets)
        for i in range(num_of_tweets - 1, max(-1, num_of_tweets - 11), -1):
            feed.append(self.tweets[i])

        heapq.heapify(feed)
        newsFeed = []
        for _ in range(min(len(feed), 10)):
            newsFeed.append(heapq.heappop(feed)[1])
        return newsFeed

class Twitter:

    def __init__(self):
        self.users = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = User(userId)

        self.users[userId].postTweet(tweetId, self.time)
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            self.users[userId] = User(userId)
        return self.users[userId].getNewsFeed()

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = User(followerId)
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)

        self.users[followerId].follow(followeeId, self.users[followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].unfollow(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

