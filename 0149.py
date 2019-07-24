class Solution:
    def maxPoints(self, points):
        if not points:
            return 0
        res = 0
        for i in range(len(points)-1):
            slopes = {}
            dup = 0
            for j in range(i+1, len(points)):
                if points[i][1] == points[j][1] and points[i][0] == points[j][0]:
                    dup += 1
                elif points[i][1] == points[j][1]:
                    if 0 in slopes:
                        slopes[0] += 1
                    else:
                        slopes[0] = 1
                else:
                    slope = (points[j][0] - points[i][0]) / (points[j][1] - points[i][1])
                    if slope in slopes:
                        slopes[slope] += 1
                    else:
                        slopes[slope] = 1
            res = max(res, max([slopes[key] for key in slopes if slopes] + [0]) + dup)
        return res + 1

