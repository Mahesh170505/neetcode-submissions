class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for Str in strs:
            sortedS = ''.join(sorted(Str))
            if(sortedS in map):
                map[sortedS].append(Str)
            else:
                map[sortedS] = [Str]
        return list(map.values())