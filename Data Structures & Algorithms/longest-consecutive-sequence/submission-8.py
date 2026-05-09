class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = list(dict.fromkeys(sorted(nums)))

        counter = 1
        longest = 1
        i = 1

        while i < len(nums):
            if nums[i] - nums[i - 1] == 1:
                counter += 1
            else:
                longest = max(longest, counter)
                counter = 1
            i += 1

        longest = max(longest, counter)
        return longest
