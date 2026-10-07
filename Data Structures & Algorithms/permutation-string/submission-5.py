class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1) - 1
        target = [0] * 26
        array = [0] * 26
        for char in s1:
            i = ord(char) - ord('a')
            target[i] += 1
        for char in s2[left : right + 1]:
            i = ord(char) - ord('a')
            array[i] += 1
        while right < len(s2):
            if array == target:
                return True
            else:
                i = ord(s2[left]) - ord('a')
                array[i] -= 1
                left += 1
                right += 1
                if right < len(s2):
                    i = ord(s2[right]) - ord('a')
                    array[i] += 1
        return False