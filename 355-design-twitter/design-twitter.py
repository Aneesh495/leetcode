
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        # Global increasing timestamp for ordering tweets
        self.time = 0
        # userId -> list of (timestamp, tweetId) in chronological order
        self.tweets = defaultdict(list)
        # userId -> set of followeeIds
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Append with current timestamp then advance clock
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # Build candidate user set including self
        users = set(self.following[userId])
        users.add(userId)

        # Max heap by timestamp using negative values
        heap = []
        for u in users:
            arr = self.tweets[u]
            if arr:
                idx = len(arr) - 1  # start from newest
                t, tid = arr[idx]
                heapq.heappush(heap, (-t, u, idx, tid))

        res = []
        while heap and len(res) < 10:
            nt, u, idx, tid = heapq.heappop(heap)
            res.append(tid)
            if idx - 1 >= 0:
                t2, tid2 = self.tweets[u][idx - 1]
                heapq.heappush(heap, (-t2, u, idx - 1, tid2))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        # Ignore self follow request
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Safe discard
        if followerId == followeeId:
            return
        self.following[followerId].discard(followeeId)
