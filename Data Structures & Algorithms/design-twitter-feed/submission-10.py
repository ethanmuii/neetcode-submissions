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
        total_posts = self.posts.get(userId, []).copy()
        for followee_id in self.following.get(userId, []):
            total_posts.extend(self.posts[followee_id])
        total_posts = [(-post[0], post[1]) for post in total_posts] # turns the UUID into a max queue for pq
        heapq.heapify(total_posts)
        ans = []
        index = 0
        while total_posts and index < 10:
            post = heapq.heappop(total_posts)
            #print(post)
            ans.append(post[1])
            index += 1
        return ans  



    def follow(self, followerId: int, followeeId: int) -> None:
        self.following.setdefault(followerId, set()).add(followeeId)
        self.followers.setdefault(followeeId, set()).add(followerId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following.setdefault(followerId, set()).remove(followeeId)
        if followerId in self.followers[followeeId]:
            self.followers.setdefault(followeeId, set()).remove(followerId)
