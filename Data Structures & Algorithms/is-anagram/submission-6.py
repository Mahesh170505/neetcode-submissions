class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr1 = list(s)
        arr2 = list(t)
        arr1.sort()
        arr2.sort()

        a = "".join(arr1)
        b = "".join(arr2)
        if(a == b):
            return True
        
        return False;
