class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()

        longest_sequence = 1
        current_sequence = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                longest_sequence = max(current_sequence, longest_sequence)
                continue
            if nums[i] == (nums[i-1] + 1):
                current_sequence += 1
            else:
                current_sequence = 1
            longest_sequence = max(current_sequence, longest_sequence)
        return longest_sequence