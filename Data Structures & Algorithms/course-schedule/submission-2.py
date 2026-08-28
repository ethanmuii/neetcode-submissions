"""
requirements:
- returning a bool if you can succesfully take all courses
- label of each course is represented through the number. i.e number 0  = course 0
- numCourses: 0 to numCourses - 1
- list of lists where each sublist represents a course # and course # you must have already taken (only 1 in this case?? NO MORE)

constraints:
- taken a course can be visualized as visited()
- cannot take a course and mark as visited until your pre-requisite is in visted
- main constraint is that because its not in the correct order of pre-requisites, you might not be able to visit/take course 0 now when you are iterating over it, but you will be able to later in the array once you visit the correct-pre requisite. 
-> can't do it in O(1) space since adding space is what you need to track it. => ADJACENCY MATRIX or if there' sosme way to find the node that doesn't have any dependencies
=> visualize a course being able to be taken with a 1. 
=> technically would be better to use an adjancency list

insights:
- prerequisites array doesn't come in proper order. 
- can visualize this as a directed graph, i.e can not visit one node until you are at the pre-requisite node and you can't get to that node until you visit its pre-requisite node. 
- RETURN FALSE when there's a cycle. => can also be visualized as a linked list. 
- a course can have itself be its pre-req meaning anyone can take it


edge cases:
- numCourse = 1, prerequisites=[0,0] should be true
"""
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjancency list and in-degree
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1

        queue = deque()
        courses_taken = 0

        # identify non-blocked courses
        for index, value in enumerate(in_degree):
            if value == 0:
                queue.append(index)
        while queue:
            curr_course = queue.popleft()
            courses_taken += 1
            possible_unlocked = graph[curr_course]
            for course in possible_unlocked:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        if courses_taken == numCourses:
            return True
        return False

        