class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()
        
        current_sequence = 1
        longest_sequence = 1

        for i, num in enumerate(nums):
            if i >= 1 and nums[i] == nums[i-1]:
                continue
            elif nums[i] == (nums[i - 1] + 1):
                current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)
            else:
                current_sequence = 1
            longest_sequence = max(longest_sequence, current_sequence)

        return longest_sequence

