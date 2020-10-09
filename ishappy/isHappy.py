class Solution:
    def newNum(self, nums: list):
        n = 0
        for num in nums:
            n = n + pow(int(num), 2)
        return n

    def getNums(self, n):
        return list(str(n))

    def isHappy(self, n: int) -> bool:
        sums = []
        while (n != 1):
            nums = self.getNums(n)
            n = self.newNum(nums)
            if n in sums:
                return False
            sums.append(n)
        return True

