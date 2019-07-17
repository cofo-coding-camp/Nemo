class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict
        def take_course(course):
            if status[course] == 1: # has cycle
                return True
            if status[course] == 2: # acyclic, pre explored
                return False
            
            status[course] = 1
            for futurecourse in graph[course]:
                if take_course(futurecourse):
                    return True
            
            status[course] = 2:
            # add to explored list
            order.append(course)
            return False
        
        # new = 0, taking = 1, finished = 2
        status = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        order = []
        for course, pre in prerequisites:
            graph[pre].append(course)
        
        for course in range(numCourses):
            if take_course(course):
                return []
        
        return order[::-1]