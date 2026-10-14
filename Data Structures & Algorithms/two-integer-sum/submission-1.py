class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}

        for i, j in enumerate(nums): 
            n = target - j
            if n in num:
                return [num[n], i]
            num[j] = i 
        return None