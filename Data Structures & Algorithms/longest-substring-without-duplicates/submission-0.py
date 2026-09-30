class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = 0 
        right = 0 
        length = 0
        ans = 0
        while left < len(s):
            while right < len(s) and s[right] not in hashSet:
                hashSet.add(s[right])
                length = (right - left) + 1
                right += 1
            ans = max(length, ans)
            hashSet.remove(s[left])
            left += 1
        return ans

            