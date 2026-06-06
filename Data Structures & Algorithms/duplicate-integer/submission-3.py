class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}

        for i, num in enumerate(nums):
            if num in prevMap:
                return True
            prevMap[num] = i
        return False