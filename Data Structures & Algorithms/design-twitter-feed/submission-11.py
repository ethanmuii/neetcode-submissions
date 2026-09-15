"""
requirements:
- each userId is unique off assumption (given to us in test case)
- each tweetId is unique off assumption (givent o us in test cases)
- we need to fetch the 10 most recent tweetIds between the user and its current following
=> ordered most recent to least recent means higher numbers are more recent
- need to track followers and following for a user in order to implement follow/unfollow function


constraints:
- getting most recent tweets -> reminds me of priority queue since it requires getting a specific invariant out of the total amount of items.
=> how do you get the most recent between a user and its followers though?
-> add all of the posts for the user and each of its following to max-pq, and then pop 10. 
-> or if each of them has more than 10, you only need to get the latest 10. 

=> do you want to store tweets in a pq or an array?

OHH TWITTER OBJECTS STORES ALL DATA ACROSS ALL USERS
- following should be a dict that stores userID and then value is list of who that user follows
- followers sshould be a dict that stores userId and then value is list of who is following that user


edge cases:
- u might try to unfollow a user that don't exist or isn't in ur following/followers
- the keys might not exist in the dictionary
- should not allow duplicates i.e don't allow a user to follow one another more than once
- higher tweetId does not mean the tweet was more recent. it basically holds no reference to when the tweet was created.  -> we need a global counter. -> posts can be stored as a list of tuples. 
=> latest tweets have a higher number
"""
class Twitter:

    def __init__(self):
        self.following = {} # key=userId, value = []
        self.followers = {} # key=userId, value = []
        self.posts = {} # key=userId, value = []
        self.UUID = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts.setdefault(userId, []).append((self.UUID, tweetId))
        self.UUID += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        total_posts = [] # this is our max heap
        candidates = [userId] + list(self.following.get(userId, set()))
        # get each candidate's newest post if it has it
        for user_id in candidates:
            user_posts = self.posts.get(user_id, [])
            if user_posts:
                last_idx = len(user_posts) - 1
                UUID, tweet_id = user_posts[last_idx]
                heapq.heappush(total_posts, (-UUID, tweet_id, user_id, last_idx - 1))

        ans = []

        while total_posts and len(ans) < 10:
            neg_uuid, tweet_id, user_id, next_idx = heapq.heappop(total_posts)
            ans.append(tweet_id)
            if next_idx >= 0:
                next_uuid, next_tweet_id = self.posts.get(user_id, [])[next_idx]
                heapq.heappush(total_posts, (-next_uuid, next_tweet_id, user_id, next_idx - 1))
        
        return ans


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)
        self.followers.setdefault(followeeId, set()).add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following.setdefault(followerId, set()).remove(followeeId)
        if followerId in self.followers[followeeId]:
            self.followers.setdefault(followeeId, set()).remove(followerId)
