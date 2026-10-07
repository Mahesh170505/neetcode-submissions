class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0 
        right = len(s1) - 1
        target = [0] * 26
        for char in s1:
            i = ord(char) - ord('a')
            target[i] += 1
        while left <= right and right < len(s2):
            word = s2[left : right + 1]
            array = [0] * 26
            for char in word:
                i = ord(char) - ord('a')
                array[i] += 1
            if array == target:
                return True
            else:
                left += 1
                right += 1
        return False