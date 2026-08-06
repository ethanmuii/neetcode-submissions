"""
solution must be O(1) space => no hash maps, only constants in variables
answer format:
- want indices, not values
- cannot use the same index twice
- first index must be lower than index 2 (same as original 2sum)
- return 1 indexed so during access of values 0-indexed, answer is index1 + 1, index2 + 1

problem:
- what does the array being ascending tell us? => can control where we look and know possible values
=> it allows us to know if we moving left or right in the array will get us a bigger number or small number
- think 2 pointer => allows us to check every combination in O(n), not checking duplicates
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 # begin index
        r = len(numbers) - 1 # end index
        while l < r:
            # 3 cases: less than target, greater than target, equal to target
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]
