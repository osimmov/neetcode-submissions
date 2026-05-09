class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # prevMap = {}

        # for i, n in enumerate(numbers):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff]+1, i+1]
        #     prevMap[n] = i

        left = 0
        right = len(numbers) - 1

        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left+1, right+1]
            elif s < target:
                left += 1
            else:
                right -= 1
        