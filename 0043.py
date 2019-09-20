class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 =='0':
            return '0'
        
        if len(num1) < len(num2):
            return self.multiply(num2, num1)
        
        num2 = num2[::-1]

        res = '0'

        for i, digit in enumerate(num2):
            temp = self.StringMultiplyDigit(num1, int(digit)) + '0' * i
            res = self.StringPlusString(res, temp)
        
        return res
        

    def StringMultiplyDigit(self, string, n):
        s = string[::-1]
        res = []
        for i, char in enumerate(s):
            num = int(char)
            res.append(num * n)
        res = self.CarrySolver(res)
        res = res[::-1]
        return ''.join(str(x) for x in res)

    def CarrySolver(self, nums):
        i = 0
        while i < len(nums):
            if nums[i] >= 10:
                carrier = nums[i] // 10
                if i == len(nums) - 1:
                    nums.append(carrier)
                else:
                    nums[i + 1] += carrier
                nums[i] %= 10
            i += 1
        return nums

    def StringPlusString(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 < l2:
            return self.StringPlusString(s2, s1)
        s1 = [int(x) for x in s1]
        s2 = [int(x) for x in s2]
        s1, s2 = s1[::-1], s2[::-1]
        for i, digit in enumerate(s2):
            s1[i] += s2[i]
        
        s1 = self.CarrySolver(s1)
        s1 = s1[::-1]
        return ''.join(str(x) for x in s1)