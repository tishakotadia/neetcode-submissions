class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ls=defaultdict(list)
        for s in strs:
            sortedS="".join(sorted(s))
            ls[sortedS].append(s)
        return list(ls.values())