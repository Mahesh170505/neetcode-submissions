class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedS = []
        for s in strs:
            encodedS.append(str(len(s)))
            encodedS.append("#")
            encodedS.append(s)
        string = "".join(encodedS)
        return string

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while(i < len(s)):
            j = i
            while(s[j] != "#"):
                j = j + 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            result.append(s[i:j])
            i = j
        return result
