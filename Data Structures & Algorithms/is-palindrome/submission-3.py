class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = "".join([char for char in s if char.isalnum()]).lower()
        reverse = "".join(reversed(char))
        if(reverse == char):
            return True
        else:
            return False