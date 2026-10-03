class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
     result = 0 
     for target in set(s):
        left = 0 
        right = 0 
        budget = k
        while right < len(s):
            if s[right] != target:
                budget -= 1
            right += 1
            while budget < 0:
                if s[left] != target:
                    budget += 1
                left += 1
            result = max(result, right - left)
     return result
