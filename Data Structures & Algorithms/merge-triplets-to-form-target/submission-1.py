"""
requirements:
- a list of lists where each sublist is 3 integers 
- unlimited amount of triplets, 1 at least. 
- only allowed to take 2 triplets and return the max of each index spot between the 2 triplets. i.e compare the same index between 2 triplets and then take the max for each index.
=> can do 0  or more times, don't need to echnically.

constraints:
- are only allowed that specific operation
- the triplets mus tbe different i.e separate indexs?
- every time we perform an operation, we are decreasing the number of total triplets i.e 2 triplets becom 1 triplet
- WE DON'T HAVE TO GET triplets down to one element, TARGET just has to be A element. 

GOAL: using the triplets + the operation, are we able to get the target operation. 

base cases/insights: 
- each index in the target triplet must exist at the correct index in any element of a triplet. -> or else its not even possible to get the target because there's no element with that value at the correct index
=> each of those values MUST be the max in its index position? and then check if it equals target?
-> this isn't true because the order matters
-> this condition is ONLY true if we end up USING that triplet. i.e you don't have to use every triplet in triplets to make target. it only has to be the max between the triplets you use

wait...
- you can only use a triplet: if the triplet's values at each index NEVER make it go over any of the target values
=> if it does, skip it and don't use it. 
=> keep track of the max_a, max_b, max_c as you iterate. 
=> if you end up with a different triplet made then its impossible to get it



=> EDGE CASE: the problem is just because the above condition exists DOES NOT guarantee a solution. this because max could overwrite a value and make it impossible to reach that value again. 

- how do you know the correct order to combine triplets?
=> lowest value in the target first?
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        max_a = 0
        max_b = 0
        max_c = 0
        for i in range(len(triplets)):
            # do we use the triplet or not?
            if triplets[i][0] > target[0] or triplets[i][1] > target[1] or triplets[i][2] > target[2]:
                continue

            # use the triplet
            if triplets[i][0] > max_a:
                max_a = triplets[i][0]
            if triplets[i][1] > max_b:
                max_b = triplets[i][1]
            if triplets[i][2] > max_c:
                max_c = triplets[i][2]
        if [max_a, max_b, max_c] == target:
            print([max_a, max_b, max_c])
            return True
        print([max_a, max_b, max_c])
        return False
        