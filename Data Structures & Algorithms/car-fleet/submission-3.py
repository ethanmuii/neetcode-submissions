
"""
- think about the problem iterations
- car fleet definition: list of indexs that were at the same position and same speed when they arrive at target
- different group of car(s) will arrive at target at different iterations or turns

- cars can't pass cars that start ahead of it -> can only move at the same speed

edge cases:
- there is no moment where one car will join another fleet and then that same car leaves to join a different fleet. not possible based on each turn
- assume each turn, every car iterates to the next position with their speed before the turn is over

- car can only travel at min(its speed, the car in front of its speed) no matter what. 

END CASE:
- we know problem is done by the time the first car's position equals target


# key breakthrough: use a stack so we cann solve it in less than O(n^2)
- the car can only as travel as the car in front of it and it can't pass it
- thus, if the car in front of it hasn't reached the target then cars before also haven't either
- these cars before it are deeper in the stack and don't need to be popped then 

does monotonic stack have anything to do with this?


NEW NOTES:
- positions aren't necessarily in sorted area, my above notes assumed that => so you can't assume later indexs mean a farther ahead starting position
=> "car cannot pass another car ahead of it" = any cars with a higher position = but doesn't necessarily assume higher index as well
==> so how do you know which cars are ahead of it? for each car?
- speeds can also be in different orders, not necessarily started


NOTES AFTER LOOKING AT HINT 1:
- you will need to sort and make an array and a bigger array that holds [position, speed] of each car.
=> so you do need the sort the array. its not possible without sorting. one of my notes was trying to think of how to do it without needing to sort 

=> why do we sort positions by DESCENDING order?***
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # make combined array
        combined = []
        combined = [[pos, spd] for pos, spd in zip(position, speed)]
        # sort the combined array
        combined.sort(key=lambda x: x[0], reverse=True)
        print(combined)
        # usint hint 3 we then make an array of time
        # then using stack would allow you to back track through the elements, remember the order of these indexs are who started closer to the finish line or had a higher position, order is desc
        # later indexs cannot pass up earlier indexs
        # this allows us to determine then when popping off the stack that if the top element isn't less than or equal to popped element, the lower elements in the stack also aren't a part of the car fleet. this is because cars cannot pass up other cars only catch up with the next one. 
        numCarFleets = 0
        stack = []
        for pos, spd in combined:
            time = ((target - pos) / spd)
            print(target, pos, spd, time)
            if not stack:
                stack.append(time)
            if stack and time > stack[-1]:
                # is ahead car have a less time than top stack, then separate fleets
                stack.append(time)

        return len(stack) # where each index in stack represents unique fleet, any car in same fleet was not added to stack, remember cars cannot pass car ahead so its same speed and fleet

        # **NEEDED ALL 4 HINTS**