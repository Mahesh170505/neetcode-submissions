class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for i in range(len(strs)):
            s = "".join(sorted(strs[i]))
            map[s].append(strs[i])
        return list(map.values())