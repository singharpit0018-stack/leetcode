class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        i = 0
        sign = 1
        
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        parsed = 0
        while i < len(s):
            cur = s[i]
            if not cur.isdigit():
                break
            else:
                parsed = parsed * 10 + int(cur)
            i += 1

        parsed *= sign

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if parsed > INT_MAX:
            return INT_MAX
        elif parsed < INT_MIN:
            return INT_MIN
        else:
            return parsed