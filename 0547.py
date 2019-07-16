# Solution - 1 DFS


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        count = 0
        l = len(M)
        fri = set()

        def DFS(i):
            for j in range(l):
                if M[i][j] and j not in fri:
                    fri.add(j)
                    DFS(j)

        for i in range(l):
            if i not in fri:
                count += 1
                DFS(i)
        
        return count


# Solution - 2 Union Find


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        l = len(M)
        circle = {i: i for i in range(l)}

        def find(i):
            if i == circle[i]:
                return i
            circle[i] = find(circle[i])
            return circle[i]
        
        for i in range(l):
            for j in range(i + 1, l):
                if M[i][j]:
                    circle[find(i)] = find(j)
        
        return sum([1 for k, v in circle.items() if k == v])