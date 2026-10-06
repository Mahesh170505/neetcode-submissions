class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0 
        right = len(s1) - 1
        while left <= right and right < len(s2):
            word = s2[left : right + 1]
            sortWord = sorted(word)
            target = sorted(s1)
            if sortWord == target:
                return True
            else:
                left += 1
                right += 1
        return False