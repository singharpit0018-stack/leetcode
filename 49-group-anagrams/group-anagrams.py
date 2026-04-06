class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for string in strs:
            cnt = [0] * 26
            for char in string:
              
                cnt[ord(char) - ord("a")] += 1 

            ans[tuple(cnt)].append(string)
            
        return list(ans.values())