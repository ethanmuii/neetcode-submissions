class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # ex. 2 = wants the top 2 most frequent elements in the array, 
        # dynamic programming? or is that used for a different frequency of elements?
        # hash map? --> can map value to the frequency of that value
        hash_map = {}
        for index,value in enumerate(nums):
            hash_map[value] = hash_map.setdefault(value, 0) + 1
        
        sorted_hash = dict(sorted(hash_map.items(), key = lambda item: item[1], reverse = True))
        solution = list(sorted_hash.keys())
        print(solution)
        solution = solution[:k]
        print(solution)
        #solution = dict(solution)
        return solution
