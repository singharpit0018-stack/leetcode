from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        longest_subs = 0
        max_chrac = 0

        freq = defaultdict(int)
        start = 0
        
        for end in range(n):
            freq[s[end]] += 1
            
            max_chrac = max(max_chrac, freq[s[end]])

            if (end - start + 1) - max_chrac > k:
                freq[s[start]] -= 1
                start += 1

            longest_subs = max(longest_subs, end - start + 1)
            
        return longest_subs