class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        d = {}

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for j in t:
            if j not in d:
                return False
            else:
                d[j] -= 1
                if d[j] < 0:
                    return False

        return True

        