class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cha1 = {}
        cha2 = {}
        for i in s:
            if i in cha1:
                cha1[i] += 1
            else: 
                cha1[i] = 1 

        for j in t:
            if j in cha2:
                cha2[j] += 1
            else: 
                cha2[j] = 1 

        if cha1 == cha2: 
            return True
        else: 
            return False
           
