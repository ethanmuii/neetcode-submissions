"""
requirements:
- length of the longest STRICTLY INCREASING subsequence (does not have to be +1 increasing) just increasing at each number
- wants subsequence, not necessarily CONSECUTIVE. -> relative order of elements has to be kept the same

constraints:
- at each element, you choose to either keep it (i.e add it to subsequence or make it the start) or leave it out of the existing subsequence. 
- let's say 9 is the start of the subsequence, any following element that wants to be included MUST BE GREATER THAN 9. if none can be included, that its max is 1 element

insights/questions
- should you keep track of the current max element in the subsequence to see if you can even include an element in the subsequence or not? 
- also ideally, you would want to dis-include a number you included, if there is a smaller numbers down the line, leaves more room to include future numbers that are increasing. 
- the possible states (i.e current subsequences) before we are at the current index must be from a max length subsequence of smaller value, not equal since strictly increasing. 

FOR EXAMPLE:
Input: nums = [0,3,1,3,2,3]
memo[0] = 1, memo[1] = 2 since 0,3 is length 2. However memo[2] = 2 again. the possible previous states memo[2] could have came from are only values that are less than nums[1] which is 0. IN a broader sense, this applies as we go down the line in future sense. 
=> Then, lets say we go to the second 3 which is memo[3]. To find its value, we index backwards and see possible valid substates where the index's value is greater than current index's value of 3. This is only 0 and 1 where memo[0] = 1 and memo[2] = 2 so we would memo[3] to equal the max between them + 1. so memo[3] = 3


CODE THAT OUT FOR NOW, but it can be optimized. -> why it should check all possible states where an index's value is less than current index's value? especially since memo[2] with value 1 was technically built off of the memo[0] = 1. -> You would be recomputing work by checking state that is guaranteed to be less than memo[1] since memo[1] included memo[0]. This is where the subproblem overlap comes in.

HYPOTHESIS: should you stop at the soonest possible previous state that is less than previous value?? will that always get the subproblem you need to build off like the max subsequence of all previous states or do you need to check a bigger search space.  Can you prove an example that breaks this hypothesis
- also need to represent not finding any previous possible state that has a lower value than subsequence. 

edge case: nums = [0, 3, 1, 3, 5, 6, 2, 3, 4]

can't disprove my hypothesis. this is because if a value is greater than the closest leftwards value that that's less than that, because it would never be possible for a farther previous value to have a value greater than the closest previous value. since that closest previous value included that farther previous value in its calculation



what does the state hold?
- could represent the max subsequence that could be created UP TO/AT number regardless of whether it includes it or NOT. i.e it represents the length of the subsequence. 

what does the transition represent?

how can it be broken down into smaller subproblems?

currently ur code stores the max increasing subsequence if you were to include that value but what if the optimal doesn't include it. 

here is a prime example that disproved both ur current code, the above point, and your previous hypothesis:
EXAMPLE: nums=[0,1,0,3,2,3]
current code at the last 3 checks 2, which checked second 0, but in reality, it should check the 1 and and then the 0. to solve this, to make each index store the MAX possible at each index or need to store a global max. 
- would taking the max of the prev i.e i - 1 and memo[prevIndex] + 1 do it? -> NO

edge case:
[4,10,4,3,8,9]
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        for i in range(1, len(nums)):
            # go back and find the first index (used for memo) of the value less than this current index
            for j in range(0, i):
                if nums[j] < nums[i]:
                    memo[i] = max(memo[i], memo[j] + 1)

        return max(memo)