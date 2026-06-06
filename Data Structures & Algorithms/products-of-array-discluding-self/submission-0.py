class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        j = 0
        res = [0] * len(nums)
        for i in range(len(nums)):
            mult = 1
            for j in range(len(nums)):
                if (j == i):
                    continue;
                else:
                    mult = mult * nums[j]
            res[i] = mult
        return res
                