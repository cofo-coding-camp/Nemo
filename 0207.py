class Solution:
    def canFinish(self, numCourses, prerequisites):
        from collections import defaultdict
        def take_course(course):
            if status[course] == 1:
                return True
            if status[course] == 2:
                return False

            status[course] = 1
            for futurecourse in graph[course]:
                if take_course(futurecourse):
                    return True
            status[course] = 2
            return False
        
        status = [0 for _ in range(numCourses)]
        graph = defaultdict(list)
        for course, pre in prerequisites:
            graph[pre].append(course)

        for course in range(numCourses):
            if take_course(course):
                return False
        
        return True 
        