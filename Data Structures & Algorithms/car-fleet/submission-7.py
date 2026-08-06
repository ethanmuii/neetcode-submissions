"""
problem insights: 
- cars that start at a higher position (i.e closer to target value) cannot be passed by cars with a lower value (i.e behind it)
- when a car joins a car fleet, it basically drives same position and same speed which means it will also take the same amount of time to reach target (as the car in front of the car fleet)
- since a car can join a fleet at destination if they arrive at the same time, you don't necessarily have to check at every interval
=> you can just check at the very end or how long it takes to reach target

- we need to sort the cars by position in a tuple of position and speed. 
- allows us to know the order of the cars and if a car can pass another car
- sort it by descending because then you put the car with no dependencies first
=> all the cars after it cannot pass it

KEY INSIGHT: - a car will join the car fleet if it has faster or equal speed to reach the target as the furthest car in the car fleet if there is one
=> or the car in front of it if there isn't one

- can just increment numFleets once you know there is a start of new one, and not increment at all when a car doesn't make a new one
=> this is valid since its the same as incrementing once you know all the cars in the fleet. its like local optimal/greedy  incrementing
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        numFleets = 0
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort(key=lambda x: x[0], reverse=True) # don't forget reverse=true. need it to be descending
        print(cars)
        times = []
        for car in cars:
            times.append((target - car[0]) / car[1])
        print(times)
        # 2 ways to do this:
        # car checks if its faster than car closest behind it
        # car checks if its faster then car at front of the fle
        # for each car, check if its faster than car in front of car fleet 
        # if there is no current carfleet, append it to front of carFleet, and increment
        # if the car is not faster than car in front of car fleet, then clear current carfleet list and add it in brand new list. this is front of current car fleet
        currCarFleet = []
        for i in range(len(times)):
            if not currCarFleet:
                currCarFleet.append(times[i])
                numFleets += 1
            elif currCarFleet and times[i] <= currCarFleet[0]:
                currCarFleet.append(times[i])
                # dont increment numFleets since it just joins existing one
            elif currCarFleet and times[i] > currCarFleet[0]:
                currCarFleet = []
                currCarFleet.append(times[i])
                numFleets += 1
        return numFleets


            
