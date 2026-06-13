class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #defaultdict creates empty list value when try to access a key that not exist, instead of throwing error.
        res=defaultdict(list)
        for s in strs:
            count=[0]*26
            for c in s:
                count[ord(c)-ord('a')]+=1
            #convert count to tuple as list is mutable, tuple is immutable, key is immutable.
            res[tuple(count)].append(s) 
        return list(res.values())