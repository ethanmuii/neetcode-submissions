"""
requirements:
- nums is all unique, no duplicates
- subsets definition: unique order does NOT matter in subsets. subsets also don't have to use every element like combinations.



constraints:
- solution can't have duplicate subsets
- want to build every possible combination where each integer in nums is a choice, and then for each path you choose an integer that hasn't been chosen and that's another choice, and you keep on going till there's nothing left to choose
=> YOU ADD IT TO FINAL ANSWER at every step, thats what makes it a subset and not a combination
=> how do you traverse every path efficiently? ->  there is n! combinations  so technically you could do like n^n time complexity.
-> O(n^2)?
=> we should use recursion or something with DFS to go down every pathway
=> if you start with 2, you don't have to go back and get 2,1 since 1,2 already covers that unique subset

edge case:
- subset includes empty list i.e nothing. -> nums = [7] means [7] and []
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        path = []
        def recursion(index, path):
        #base case
            if index == len(nums):
                ans.append(path[:])
                return
            # choose the element
            path.append(nums[index])
            recursion(index + 1, path)
            path.pop()
            # recurse down the path of the next element and don't choose the element
            recursion(index + 1, path)



        recursion(0, path)
        return ans

        