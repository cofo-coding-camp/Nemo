# Solution 1 - brutal force (Time Out)


class Solution:
    def bulbSwitch(self, n: int) -> int:
        res = 0
        for i in range(n):
            counter = 0
            for j in range(n):
                if (i + 1) % (j + 1) == 0:
                    counter += 1
            if counter % 2:
                res += 1
        
        return res

# Solution 2 - ???


from math import sqrt
class Solution:
    def bulbSwitch(self, n: int) -> int:
        return int(sqrt(n))