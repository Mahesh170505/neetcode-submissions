class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 0
        for var in set(s):             
            l = k
            left = right = 0
            while right < len(s):
                if s[right] == var:
                    right += 1
                elif l > 0:
                    l -= 1
                    right += 1
                else:
                    if s[left] != var:
                        l += 1
                    left += 1
                length = max(length, right - left)
        return length