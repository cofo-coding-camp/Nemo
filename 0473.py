class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        if sum(nums) % 4 or not nums:
            return False
        l = sum(nums) // 4
        edge = [0] * 4
        nums.sort()
        if nums[-1] > l:
            return False

        self.res = False

        def backtrack(cur, nums, l, temp=[0] * 4):
            if self.res:
                return
            if cur == -1:
                for val in temp:
                    if val != l:
                        return
                self.res = True
                return
            for i in range(4):
                last = temp[i]
                temp[i] += nums[cur]
                if temp[i] <= l:
                    backtrack(cur-1, nums, l, temp)
                temp[i] = last

        backtrack(len(nums)-1, nums, l)
        return self.res