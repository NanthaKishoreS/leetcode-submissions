class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        l=len(strs)
        max_len = min(len(strs[0]),len(strs[l-1]))
        i=0
        while i < max_len:
            if strs[0][i] == strs[l-1][i]:
                i = i + 1
            else:
                return strs[0][:i]
        return strs[0][:i]
        
                
        