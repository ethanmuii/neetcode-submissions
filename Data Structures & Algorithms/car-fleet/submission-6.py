"""
n cars. 
positioni[i] represents the starting position of the ith car
speed[i] represents the speed of the ith the car


cars behind that car's starting position can never pass it (one way high way) can only catch up to it and then go same speed.
=> i.e join its car fleet.
=> realized that you don't have to start counting car fleets at the very end at target, can assume it whenever. 

ans: return the number of different groups that arrive at target. 
if group of cars reach the target at the same time, then it is considered 1 car fleet (i.e reach target at the same time)

to see when a car arrives at target (like after how many intervals/hrs): (target - position[i]) / speed[i]

however, remember a car that starts behind another car cannot pass it even if it reaches it in less intervals. 

how do we know the order of the cars -> sorting it, ascending or descending and why?
=> descending. this is because everything depends on the car most in front since nothing can pass it. 
=> this car should be the leftmost
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # edge case:
        if len(position) == 0:
            return 0
        
        # make the combined array
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0], reverse=True) # make it descending
        print("cars: ", cars)
        # now need to compute the intervals it takes a car to reach target
        times = []
        for car in cars:
            interval = (target - car[0]) / car[1]
            times.append(interval)
        print("times: ", times)
        
        # if carA's interval is < carB's interval in front of it then increment numFleet.
        # if carA's interval is >= carB's interval that means carB will catch up it and it becomes interval. You don't know if it when the fleet ends until a car is faster than the next car behind. 
        
        # how to handle the check of last element that might index out of bounds
        fleets = []
        currFleet = []
        fleetTime = times[0]
        for i in range(len(times)):
            if times[i] > fleetTime:
                fleets.append(currFleet)
                currFleet = [i]
                fleetTime = times[i]
            elif times[i] <= fleetTime:
                currFleet.append(i)
        
        fleets.append(currFleet)

        return len(fleets)
        
        
        
        
        
        
        
        for i in range(len(times)):
            print(len(times), i)
            if i + 1 >= len(times):
                if times[i] > times[i - 1]:
                    fleets.append(currFleet)
                    currFleet = []
            elif times[i] < times[i + 1]:
                fleets.append(currFleet)
                currFleet = []
            else:
                currFleet.append(i)

        if currFleet:
            fleets.append(currFleet)

# (4, 1) (2, 3) (0, 2)

        return len(fleets)


        