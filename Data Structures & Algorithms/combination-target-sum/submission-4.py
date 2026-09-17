"""
requirements:
- given unique integers, no duplicates
- target integer
- return list of all combinations that sum to target. NO DUPLICATE COMBINATIONS (don't add to final array if its the same) -> maybe need a set?
=> combination can be of any length in this scenario (so basically subsets)

constraints:
- no duplicate combinations: combination is same freq of every number
=> how do you prevent duplicates?


- can use any number in nums, an unlimited amount of times -> SO HOW DO WE KNOW WHEN TO STOP?
=> if at any point, ur current path is > target, you need to prune and stop. you shouldn't even keep on going down the line IF UR initial array is sorted. technically could sort and it wouldn't be bad cuz overall time complexity will be worse than O(nlogn) => prune early to save time

edge case:
- since you have distinct integers in nums, there's no chance that there is another number that follows up and is same as a prev one you've seen like [2, 2, 2] where you try to check 2 multiple times if target = 2. 
- i think once you move onto the next number, thus eliminating at least 1 number, it prevents you from forming the same combinations again

- current code is some how having duplicates?

"""
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        path = []
        nums.sort()
        def recursion(index, total, path):
            if index == len(nums): # no out of bounds
                return
            # choose this element
            if total + nums[index]> target:
                return

            path.append(nums[index])
            total += nums[index]
            if total == target:
                ans.append(path[:])
                path.pop()
                total -= nums[index]
                return
            else:
                recursion(index, total, path) # can use the number unlimited amount of times
                # pop and backtrack
                path.pop()
                total -= nums[index]
            # skip the element
            recursion(index + 1, total, path)



        recursion(0, 0, path)
        return ans