class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # arr = set(nums)
        # if len(arr) < len(nums):
        #     return True
        # else:
        #     return False

        dict_nums = set()

        for num in nums:
            if num in dict_nums:
                return True
            dict_nums.add(num)
            
        return False