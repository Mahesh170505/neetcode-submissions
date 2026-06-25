class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = "".join(char for char in s if char.isalnum()).lower()
        i = 0
        reverse = []

        for j in range(len(word) - 1, -1, -1):
            reverse.append(word[j])
        
        reverseS = "".join(reverse)
        if(reverseS == word):
            return True
        
        return False