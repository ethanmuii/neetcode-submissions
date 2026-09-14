"""
requirements:
- given array of uppercase english letters where task[i] is A LETTER.
- you can view each index as a distinct task, but let's say SAME LETTERS are the same TYPE OF task
- given 'n', the number of CPU cycles that must seperate same type of tasks. 


constraints:
- the same type of task must be separated by n CPU cycles, can't be processed until that many have cycles have passed since we processed that one initially. 
- we can process the tasks in ANY ORDER -> but what is the optimal order
- we want to return the MINIMUM number of CPU cycles required to complete all tasks. -> this means we want to minimize the number of IDLES. 

insights:
- need to keep track of how CPU cycles have passed since we last processed a task of that type. -> this allows us to know whether we can/when we can process a task of that type
- the optimal order to process the task is to process the most frequent task type first so you can put less frequent items in between those i.e if you don't process the most frequent tasks first, you are going to have to use IDLES instead of consuming tasks while u wait for CPU to cooldown for that specific task

1) need a hashmap to keep track of the frequency count of all tasks -> allows us to know what is the MOST FREQUENT element currently in O(1) time. -> just decrement it every time you process it. 
=> could have a seperate counter of total tasks and once that hits zero return, or you could just see if hashmap is empty? 



other solution idea:
- what if we have a priority queue that stores the like ticks, and  the freq of that task
=> we should prioritize the the tasks with the lower amount of ticks, where the first entry of that task should be like 0 ticks, and the second entry of that same task should be like +n ticks i.e it can't be processed until we have that amount of ticks.
==> now how do we process the most frequent task first since technically all distinct tasks are going to have 0 ticks required => our tie breaker can be the freq of the element
=> I'm assuming the frequency of the element won't change and it wont change because you can't keep on processing the most frequent element so it will stay the most frequent element throughout.
=> we won't know the task itself, but we don't need too we just need to know how many CPU cyles it goes thru


edge case:
- the most popular type of task might not always come first
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        total_cycles = 0
        # build freq hashmap of tasks
        freq_counter = {}
        for task in tasks:
            freq_counter[task] = freq_counter.setdefault(task, 0) + 1

        # make max_heap
        max_heap = []
        for key, value in freq_counter.items():
            heapq.heappush(max_heap, value * -1)

        # initialize cooldown # stores when a task becomes avaliable 
        cooldown = deque()

        # iterate while you have avaliable tasks or tasks in cooldown
        while max_heap or cooldown:
            total_cycles += 1

            # now add items in cooldown back to max_heap if its current_time equals 
            if cooldown and cooldown[0][1] == total_cycles:
                current = cooldown.popleft()
                heapq.heappush(max_heap, current[0])

            if max_heap:
                top = heapq.heappop(max_heap)
                top += 1 # reverse decrementing since its negative
                # add it to cooldown
                if top != 0:
                    cooldown.append((top, total_cycles + n + 1))
            
        return total_cycles
        