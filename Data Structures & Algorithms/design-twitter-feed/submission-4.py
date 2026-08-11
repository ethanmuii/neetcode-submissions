"""
the init is the system itself, not a specific user. => what does the system need to keep track off
- hashmap for followers, following, and tweets? 

the biggest constraint we need to account for is in getNewsFeed():
- are tweetids ordered in some specific way? i.e more recent tweet IDs have a higher number? 
- ordered most recent to least recent. i.e higher numbers to lower numbers??
- use a priority queue and calculate it on the fly? don't store it in init for each user since it becomes tricky when users follow and unfollow someone. 
- ALL THE OTHER FUNCTIONS affect which shows up on postTweet


edge case:
- do we have to worry about null handling? can the user call getNewsFeed when there is no tweets to show meaning we would have to return null or handle hashmap not erroring out.
- there aren't 10 tweets to show in newsFeed.
- need to handle proper reading of values in hashmaps, especially if key doesn't exist. 
- tweetIds are not ORDERED where most recent global tweets have higher IDS. they are still unique though. need a global counter for each posted tweet
- users can't follow themselves => thus can't unfollow themselves (but this case won't happen unless they follow themselves)
"""
class Twitter:

    def __init__(self):
        self.followers = {} # key = userId, value = set of userIds
        self.following = {} # key = userId, value = set of userIds
        self.tweets = {} # key = userId, value = list of tweetIds
        self.global_tweet_counter = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.setdefault(userId, []).append((self.global_tweet_counter, tweetId))
        self.global_tweet_counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # for each person the userId is following, take their list of tweets and make one big list and then heapify it. and append 10 most recent to the list.
        master_tweets = []
        master_tweets.extend(self.tweets.setdefault(userId, []))
        if userId == 1:
            print(master_tweets)
        for person in self.following.setdefault(userId, set()):
            master_tweets.extend(self.tweets[person])


        max_heap = [(-x[0], x[1]) for x in master_tweets]
        heapq.heapify(max_heap)
        ans = []
        index = 0
        while max_heap and index < 10:
            top = heapq.heappop(max_heap)
            print(top)
            ans.append(top[1])
            index += 1
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.followers.setdefault(followeeId, set()).add(followerId)
        self.following.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId == 1 and followeeId == 2:
            print("before", self.followers[followeeId], self.following[followerId])
        if followerId in self.followers.setdefault(followeeId, set()):
            self.followers.setdefault(followeeId, set()).remove(followerId)
        if followeeId in self.following.setdefault(followerId, set()):
            self.following.setdefault(followerId, set()).remove(followeeId)
        if followerId == 1 and followeeId == 2:
            print("after", self.followers[followeeId], self.following[followerId])
