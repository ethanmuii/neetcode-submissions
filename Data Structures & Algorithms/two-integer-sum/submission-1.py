class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force by just checking every possible combination of pairs
        # how can we implement it using HASH MAP?
        # returning the INDEX , NOT values
        # return smaller index
        visited = {}
        solution = []
        for index, value in enumerate(nums):
            wanted = target - value
            if wanted in visited:
                solution.append(visited[wanted])
                solution.append(index)
            else:
                visited[value] = index
        return solution

        