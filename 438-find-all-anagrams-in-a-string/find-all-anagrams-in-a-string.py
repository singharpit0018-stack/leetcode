class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res= []
        p_Counter=Counter(p)
        s_Counter =Counter(s[:len(p)])

        for i in range(len(s)-len(p)):
            if p_Counter==s_Counter:
                res.append(i)
            s_Counter[s[i]]-=1

            if s_Counter[s[i]]==0:
                del s_Counter[s[i]]

            s_Counter[s[i+len(p)]]+=1
        
        if s_Counter== p_Counter:
            res.append(len(s)-len(p))
        return res


        
        