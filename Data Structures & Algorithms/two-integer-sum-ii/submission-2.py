class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(numbers, start=1 ):
            diff = target - n
            if diff in prevMap:
                return [numbers.index(diff)+1, i]
            prevMap[n] = numbers[i]
        return