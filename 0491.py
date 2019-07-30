class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        idx_map = {nums[0]: -1}

        for i in range(1, len(nums)):
            if nums[i] not in idx_map:
                idx_map[nums[i]] = len(res)
                res += [lst + [nums[i]] for lst in res if lst[-1] <=nums[i]] + [[nums[i]]]
            else:
                temp = len(res)
                res += [res[j] + [nums[i]] for j in range(temp) if res[j][-1] <= nums[i] and j >= idx_map[nums[i]]]
                idx_map[nums[i]] = temp
        return [lst for lst in res if len(lst) > 1]