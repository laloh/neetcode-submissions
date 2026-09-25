class Twitter:

    def __init__(self):
       self.follows = {}
       self.tweets = {}
       self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        
        self.time += 1
        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        if userId in self.tweets:
            for time, tweetId in self.tweets[userId]:
                heapq.heappush(feed, (-time, tweetId))

        followers = self.follows[userId] if userId in self.follows else []

        for followerId in followers:
            for time, tweetId in self.tweets[followerId]:
                heapq.heappush(feed, (-time, tweetId))

        mostRecentFeed = []
        k = 10

        while feed and k > 0:
            time, tweetId = heapq.heappop(feed)
            mostRecentFeed.append(tweetId)
            k -= 1

        return mostRecentFeed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()

        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows or \
           not self.follows[followerId]:
            
            return
        
        self.follows[followerId].remove(followeeId)
