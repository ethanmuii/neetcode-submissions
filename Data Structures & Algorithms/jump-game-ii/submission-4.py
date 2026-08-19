"""'
- trying to build intution, after seeing visual explanation
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l = 0
        r = nums[0]
        min_hops = 1
        # as soon as your r reaches the end index, thats when its in your range and you found the min number of hops to reach it
        while r < len(nums) - 1:
            curr_index = l
            farthest_index = r + 1
            # iterate through the current range to find the farthest index you can reach
            while curr_index < len(nums) and curr_index <= r: 
                farthest_index = max(farthest_index, curr_index + nums[curr_index])
                print(farthest_index)
                curr_index += 1

            # increment min_hops, and the move the next range you can reach in min hops
            l = r + 1
            r = farthest_index
            print(l, r)
            min_hops += 1

        return min_hops