"""
this problem is a more specific version of the last. -> just need to return the valid ordering. NOT ALL VALID ORDERINGS, just a valid ordering. if you can't taken all of them, return an empty array. 
"""
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build adjancency list and in-degree
        graph = {i: [] for i in range(numCourses)}
        in_degree = [0] * numCourses
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
            in_degree[prereq[0]] += 1

        queue = deque()
        courses_taken = 0

        # identify non-blocked courses
        curr_path = []
        for index, value in enumerate(in_degree):
            if value == 0:
                queue.append(index)
        while queue:
            curr_course = queue.popleft()
            curr_path.append(curr_course)
            courses_taken += 1
            possible_unlocked = graph[curr_course]
            for course in possible_unlocked:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    queue.append(course)

        if courses_taken != numCourses:
            return []
        return curr_path        