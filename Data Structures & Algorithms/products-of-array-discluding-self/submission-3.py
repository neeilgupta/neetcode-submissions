class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        #prefix calc
        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        
        return res


            
                