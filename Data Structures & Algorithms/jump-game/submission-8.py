"""
requirements:
- return bool condition
- array guaranteed to exist with 1 element
- no negative elements

constraints:
- can you reach the last index?
- value at nums[i] determines how many indexs you can jump or what index can you get to AT A MAXIMUM,
- meaning you can choose any number of indexs to jump from 0 to nums[i]] from i

insight:
- there's multiple branches to try. technically at each index, you try nums[i] possibilities to jump to. 
=> you want to skip any possible branches if the nums[i] is 0 because then it's a dead spot
=> DO YOU ALWAYS WANT TO TAKE THE HIGHEST JUMP i.e nums[i] or does it depend on situation? -> you obviously don't want to jump 0 and want to avoid all 0's unless its the last ending spot. 
==> not necessarily because consider this test case: nums = [1,2,2,0,0]
=> out of all your options, do you want to take the jump to the spot that has the highest nums[i] so in the above example it wuold be jump + 1 index and land at 2. 
==> don't necessarily have to reach it in the most efficient way, just have to get there or see if we can. 
=> can index the indices in O(1) since its an array and can access them with addition.

yes, you want to land at the place that has the highest jumping power because anywhere with the highest jumping power will move you closer to your end index and extend your possible range of choices to make you closer.
=> ex. nums = [3,5,0,4,0,0,0]  , you can jump straight to 4 and do it, or you can jump to 5 and then 5 can still get to 4 so it doesn't matter. you are guaranteed to be able to reach the same spots by taking the highest number within range

- why can't you just take any number that is greater than 0? like the first one you see because it migh tblock off choices like this ex. [3,1,0,4,0,0,0] 


when should you a landing spot that you have an option?
- given all my notes/insights in the above: you shouldn't take the spot with the highest jumping power out of your options. -> YOU should only take a spot if it can take you farther than what your currennt index has access to. 
=> my above insight made the assumption that the highest jumping spot you can land will always take you farther than what the current index can access but that's not necessarily true (regardless of whether the correct landing spot is 0) => remember we just want to get to the end. 

edge case:
- element wiht 1 element, and its 0. => true, you are at last index
nums=[1,2,2,0,0] -> need to make sure to take the farthest index if there is even jumping power?
- proves my theory wrong: nums=[3,0,8,2,0,0,1]
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr_index = 0
        last_index = len(nums) - 1
        # use while loop because you might have to check a val twice and you aren'y iterating in + 1 increments
        while curr_index < last_index:
            curr_jump_length = nums[curr_index]
            print(curr_jump_length)
            reach_index = curr_index + curr_jump_length
            print(reach_index)
            next_index = curr_index + curr_jump_length
            for i in range(curr_jump_length):
                # defaults
                # update the max spot only if a landing spot can take you even farther, else it just defaults to the max jump length that curr_index can go
                if curr_index + i <= last_index and nums[curr_index + i] + curr_index +  i > reach_index:
                    reach_index = nums[curr_index + i] + curr_index + i
                    next_index = curr_index + i

            # update the curr_index
            curr_index = next_index
            print(curr_index)
            # if you land on a dead spot where you equal 0, you gotta stop
            if curr_index >= last_index:
                return True
            if nums[curr_index] == 0:
                return False
        return True