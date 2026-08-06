"""
problem: k represents the number of elements that need to get returned, and those elements that are the most frequent
k = 2, => 1st most frequent element, 2nd most frequent element

answer: order doesn't matter, return a list of the numbers, NOT indices


hash map solution: key = number, value = count of that number, and then sort the by values? and return the keys

time complexity: O( N LOG N) and space complexity: O(n)


could also do a priority queue with tuples
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        desc_list = (sorted(hashmap.items(), key=lambda item: item[1], reverse=True))

        # ans
        ans = []
        for i in range(k):
            ans.append(desc_list[i][0]) # [0] gets the number and not the count

        return ans

        