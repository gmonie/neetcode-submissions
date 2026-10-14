class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        frec = {}
        for i in nums: 
            if i in frec: 
                return True
            else:
                frec[i] = 1
        return False
        