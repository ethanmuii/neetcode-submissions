"""
REACTO

- input: list of nums
- need to return the k frequent elements in the array
- based on the examples, it sounds like k = 2, means return the 1st most frequent element and the 2nd most frequent element

APPROACH: 
- hash map: key = number, value = frequency
- then add all these values to a PQ, and pop k times, and each value gets added to a list (where the list is the answer)

QUESTIONS:
- is the array always sorted  -> NO
"""

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = dict()
        res = []
        freq_elements = []
        for num in nums: 
            hmap[num] = hmap.get(num, 0) + 1
        print(hmap)
        # priority queue using heapq is a MIN-HEAP always by default. This is why -1 is needed. 
        for key, value in hmap.items():
            heapq.heappush(freq_elements, (value * -1, key))
        print(freq_elements)
        for i in range(k):
            pair = heapq.heappop(freq_elements)
            print(pair)
            val = pair[1]
            res.append(val)
        return res

# TIME COMPLEXITY is O(n) where n is the length of nums. O(n) space complexity where n is the length of nums since it a hash map of length n, and a priority queue of lenght n before popping. 

        