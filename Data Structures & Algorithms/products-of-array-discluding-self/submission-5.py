class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        if not nums:
            return 0

        #left pass
        left_prod = 1
        left = [1] * len(nums)
        for i in range(len(nums)):
            left[i] = left_prod
            left_prod *= nums[i]


        #right pass
        right_prod = 1
        right = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            right[i] = right_prod
            right_prod *= nums[i]
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
        return res

