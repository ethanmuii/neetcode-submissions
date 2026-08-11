"""
requirements:
- want the MINIMUM # of cycles to get rid of all of the tasks

constraints:
- identical tasks (i.e tasks with the same letter) must be separated by AT LEAST "n" CPU cycles
- you can only choose/use/pop one task i.e letter per cycle. 
- you can process the tasks IN ANY ORDER (as long as it meets the first constraint)

overall goal: given above constraints, we ideally want to process one task in tasks each cycle so no cycles are going to waste not processing a task because the only thing that was left was an identical task and we can't process it because of the "separated by at least n CPU cycle contraint"

how will you handle duplicate tasks? -> this is the bottleneck
- we can process tasks in any order, but how will we know what tasks are even avaliable to choose from? 
=> we must iterate over tasks O(n) time to know which tasks are avaliable and after each cycle + how many types of tasks or the freq per task

possible solution:
- iterate over tasks in O(n) time. and use a hashmap where key = letter, value = freq of that letter?
=> allows you access and decrement identical tasks in O(1) time, but you don't remember the keys

- use a priority queue, where its either max or min? the priority determines which tasks should come out and in what order? given the constraints like can't process identical tasks unless separated by N CPU cycles

- priority queue, and track prevTask, keep on going until pq is empty, and don't pop unless it meets above constraints?
=> what determines priority when you are adding these tasks to the queue. 
=> would be tuple of (priority, "task letter")
=> non-identical task should have a higher priority than an identical task
=> all tasks that are first-time, no-existing identical, should have a min priority of 0.

edge case:
- because we can process in any order, identical task doesn't necessarily have to be next to in the array, its globally based on the freq count of that task (i.e HASH MAP)
- you have to wait an idle cycle until you can process an identical task (only identical tasks left)


EDGE CASE (need to pay attention to better examples):
- just becaue you processed a different task doesn't mean the separation counter resets.
- identical task need to be separated by n CPU cycles regardless of whether you process a different one

- either update to priority in min_pq to account for these changes?
- dont pop from pq unless it meets these conditions?
- current solution does: X -> Y -> X -> Y, but needs to be idle in between Y and X. how can you remember if it has or hasn't been N CPU cycles. 
=> something to do with min_intervals??
"""
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        min_intervals = 0 # i.e time
        task_freq = {}
        for task in tasks:
            # just make the freq 1-indexed
            task_freq[task] = task_freq.get(task, 0) + 1
        # task freques inserted into max_heap
        max_heap = []
        for key, value in task_freq.items():
            heapq.heappush(max_heap, (-value, key))
        # initialize queue to enforce cooldown of each task that has been processed
        queue = deque()
        # end condition: once both max_heap and queue are empty, no tasks are on cooldown and no tasks are waiting to be processed
        while max_heap or queue:
            if not max_heap:
                min_intervals = queue[0][0]
                #print(min_intervals)
                left = queue.popleft()
                heapq.heappush(max_heap, (-task_freq[left[1]], left[1]))

            elif max_heap:
                top = heapq.heappop(max_heap)
                task_freq[top[1]] = task_freq.get(top[1], 0) - 1 # decrement the freq of the task
                min_intervals += 1 # increment the cycle that has passed
                #print(top[1], min_intervals)
                # only want to append to queue if the count is not 0 i.e all of the tasks for that letter have NOT been processed
                if task_freq[top[1]] > 0:
                    queue.append((min_intervals + n, top[1])) # append (time they become avaliable after the cooldown, task letter) to queue
                # check the task at front of the queue
                if queue and min_intervals >= queue[0][0]:
                    left = queue.popleft()
                    #print(left)
                    heapq.heappush(max_heap, (-task_freq[left[1]], left[1]))
            
        return min_intervals


            

        