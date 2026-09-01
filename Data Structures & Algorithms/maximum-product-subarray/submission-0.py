"""
requirements:
- want the largest product and need to return it of a SUBARRAY
- values in the array can be negative, 0, or positive

constraints:
- subarray must be a consecutive elements multiplied together, can't pick n choose ones. either you pick it and add to previous subarray or you start a new consecutive subarray from that element.
- need to be tricky when dealing with negative numbers. 
=> negative numbers are only beneficial when there is an even amount used in the consecutive sequence, if there is an odd amount, or an even amount CAN'T be used consecutively, then it isn't that beneficial.
- NOT KNOWING HOW MANY NEGATIVE VALUES YOU HAVE IN THE FUTURE with your current subsequence

insights:
- at each element, you want to either multiply the element by the current subsequence or you want to start over. 
=> nums = [2,4,-3,5] -> the highest product with just 2 is 2, with 4 it becomes 8. then with -3 you either want to multiply it by 8 or start over from -3. starting over from negative 3 would give you a better start. then you do you want to multiply -3 by 5 or just start with 5, you would want to start with 5 instead of -15. HOWEVER, 5 IS NOT THE RIGHT ANSWER SO EITHER YOU NEED TO TRACK GLOBAL MAXIMUM or make the previous subproblems that 5 depends have the global max. 
=> insight -> well what if there was another negative number after 5 like -1, then technically you would want to keep everything 2 * 4 * -3 * 5 * -1 which would give you 15 * 8 = 120. but in your code, you would start over from -3 instead of multiplying 2 8 * -3 and keeping it in the current subsequence. 
- double for loop encapsulates all the possible ranges of subarrays that could be created and you want the max from it.
- if you see a positive value in the current consecutive subarray, YOU MUST TAKE IT. it can only help, it can never be bad. the only weird case is negative numbers. 

what should the state hold?
- not the global max that will likely have to be separate because you don't know if you are including the value
- multiple iterations of the dp problem where you move the starting point over by 1 and take the maxmimum out of all possible DP's ran per starting point? -> that's basically O(n^2) though. 

- what if you just take the abs max each time, but store the real number in the memo? 
nums = [2, 4, -3, 5] = memo[2, 8, -24, -120] but what if it was [2, 4, -3, 10] = memo[2, 8, -24, -240] but the optimal answer should be 10 out of that memo. but  if it was [2, 4, -3, 10, -1] then the optimal answer becomes 240 not 10
=> its like i wish we could store both options like us multiplying by existing subsequence or starting over. => CAN'T KNOW WHICH ANSWER WOILL BE OPTIMAL UNTIL WE KNOW HOW MANY NEG NUMBERS ARE IN THE SUBARRAY
- we can't just take the local max between including it versus starting over as proved wrong.
- we also can't just always take including it and multiplying it. 


WAIT:
- what if we always want to take negative values like include it in the starting subsequence in hopes that a future negative comes. never want to start over from it since it will never be greater than an existing previous subarray that was originally all positive.
- the question comes down when you current subsequence is negative and you have a positive value, when should you take it? -> when there is another negative value on the other side, if its just a positive, then start over. 
=> should we store the number of future negative numbers including the starting index to the end at each index? -> that could solve our problem. if there is an even number, then take the positive number, if its odd then start over? 

edge cases:
- single element array should just returned that element. 
- [2,4,-3,5, -1] -> technically want to keep all values. 
- [-1, 3, 4, 5, 6] -> in this case you would want to start over the subsequence starting with 3. don't keep the -1. 


SOLUTION: just track both the maximum and minimum of each i, that is how you prevent not knowing the future
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        global_max = nums[0]
        for i in range(1, len(nums)):
            prev_max = current_max
            prev_min = current_min
            current_max = max(prev_max * nums[i], prev_min * nums[i], nums[i])
            current_min = min(prev_max * nums[i], prev_min * nums[i], nums[i])
            global_max = max(global_max, current_max)

        return global_max

        