class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {} 

        for l in s : 
            if l in first: 
                first[l] += 1 
            else: 
                first[l] = 1

        for l in t : 
            if l in second: 
                second[l] += 1 
            else: 
                second[l] = 1

        if first == second : 
            return True 
        else: 
            return False
       