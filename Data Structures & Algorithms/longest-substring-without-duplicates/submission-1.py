class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        length = 0
        result = 0
        left = 0
        right = 0
        while left < len(s):
            while right < len(s) and s[right] not in hashSet:
                hashSet.add(s[right])
                length = right - left + 1
                right += 1
            result = max(result, length)
            hashSet.remove(s[left])
            left += 1
        return result