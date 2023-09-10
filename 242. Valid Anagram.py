class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        diction_s = {}
        diction_t = {}

        for i in s:
            if diction_s.get(i) == None:
                diction_s[i] = 1
            else:
                diction_s[i] += 1

        for i in t:
            if diction_t.get(i) == None:
                diction_t[i] = 1
            else:
                diction_t[i] += 1
        
        if diction_s == diction_t:
            return True

        return False

