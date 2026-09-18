class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            sum = 0
            for ch in word:
                sum = sum + weights[ord(ch)-97]

            letter = chr(122 - (sum % 26))
            res = res + letter

        return res
            
        
        