class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            sortedS = ''.join(sorted(str))
            map[sortedS].append(str)
        return list(map.values())
                
