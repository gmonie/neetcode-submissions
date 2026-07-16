class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {} 

        for i, n in enumerate(nums):
            com = target - n

            if com in num:
                return [num[com], i]

            num[n] = i