class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Map = dict()
        result = list()
        for word in strs:
            sort = sorted(word)
            final = "".join(sort)
            if final in Map:
                Map[final].append(word)
            else:
                Map[final] = [word]
        return list(Map.values())