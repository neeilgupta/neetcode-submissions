class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        #Left Pass
        left_product = 1
        left_array = [1] * len(nums)
        for i, n in enumerate(nums):
            left_array[i] = left_product
            left_product = left_product * n
        #Right Pass
        right_product = 1
        right_array = [1] * len(nums)
        for j in range(len(nums) - 1, -1, -1):
            n = nums[j]
            right_array[j] = right_product
            right_product = right_product * n
        for k in range(len(nums)):
            res[k] = left_array[k] * right_array[k]
        return res