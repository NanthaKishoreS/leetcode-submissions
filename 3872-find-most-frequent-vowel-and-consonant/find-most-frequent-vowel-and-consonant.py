class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = "aeiou"

        v = {}
        c = {}

        for ch in s:
            if ch in vowels:
                v[ch] = v.get(ch,0)+1
            else:
                c[ch] = c.get(ch,0)+1

        vmax = max(v.values(),default=0) 
        cmax = max(c.values(),default=0)

        return vmax+cmax
