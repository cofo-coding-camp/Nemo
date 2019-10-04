class Solution:
    # Solution 1 - O(n^3)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        
        nums.sort()
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
                continue

            for j in range(i + 1, n - 2):
                if j - i > 1 and nums[j] == nums[j - 1]:
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
                    continue
                left = j + 1
                right = n - 1
                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    if temp == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif temp > target:
                        right -= 1
                    else:
                        left += 1
        
        return res

    
    # Solution 2 - O(n^2)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        from itertools import combinations

        dic, l = defaultdict(list), [*combinations(range(len(nums)), 2)]
        for a, b in l:
            dic[target - nums[a] - nums[b]].append((a, b))
        r = [(*ab, c, d) for c, d in l for ab in dic[nums[c] + nums[d]]]

        return [*set(tuple(sorted(nums[i] for i in t)) for t in r if len(set(t)) == 4)]