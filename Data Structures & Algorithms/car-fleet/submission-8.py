"""
- return the NUMBER of different car fleets at destination
- each car fleet is at the same position and same speed

- how do cars join another car fleet?
- the car behind it as to have "caught up with the car in front", and then it cannot overtake the car even if it can arrive to the destination faster. it adopts to the position and speed of the fleet

the min speed of the fleet is always the car at the very front or the min because if the car at the very front didn't have the min speed, the cars behind it never would have caught up. the position is always the max and since the fleet will start at the very first car and the car must always be in the front since there is no passing

ideal solution:
- we can apply the concepts above to time itself -> time it takes to reach destination
=> (destination - position[i]) / speed[i]
- for a car fleet, this value is always the first car in the fleet. 
- when a car joins the fleet, its time value becomes the max of the fleet.  i.e it can only drive as FAST as the slowest car in the fleet which would be the front car. it cannot overtake cars. 
=> if the front car was faster than everyone else, no one would catch up adn it would be a different fleet. 

edge cases:
- if multiple cars join the fleet, you need to compare the time to the slowest car in the fleet (i.e the first car in the fleet), not the car in front of it. this is because the car in front of it (i.e next index) might no longer take that time, instead it could have joined the car fleet and is now driving only as fast as the slowest car in the fleet i.e the first car. 
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # need to first sort the cars by position. with the first car being the highest position
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        sorted_cars = sorted(cars, key=lambda x:x[0], reverse=True)
        # now that cars are sorted by furthest cars in front at beginning, need to calculate each cars time to reach destination
        times = []
        for i in range(len(sorted_cars)):
            time = (target - sorted_cars[i][0]) / sorted_cars[i][1]
            times.append(time)

        # need to count the number of car fleets
        # number of car fleets only goes up when WE CREATE A NEW FLEET
        curr_fleet = []
        num_fleets = 0
        for i in range(len(times)):
            if not curr_fleet:
                num_fleets += 1
                curr_fleet.append(times[i])
            else:
                if times[i] <= curr_fleet[0]: # a car is faster or just as fast as first car in fleet
                    curr_fleet.append(times[i]) # this is techncially useless
                else: # a car is not as fast or faster so new fleet is created
                    curr_fleet = [times[i]]
                    num_fleets += 1
        return num_fleets

        