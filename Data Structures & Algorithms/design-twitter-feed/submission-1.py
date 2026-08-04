from collections import defaultdict
import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time +=1

        self.tweets[userId].append((self.time,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:

        user = set(self.follower[userId])
        user.add(userId)
        
        minHeap = []

        for u in user:
            for tim,tweet in self.tweets[u][-10:]:
                heapq.heappush(minHeap,(tim,tweet))

                if len(minHeap) > 10:
                    heapq.heappop(minHeap)

        res = []
        while minHeap:
            res.append(heapq.heappop(minHeap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].discard(followeeId)
