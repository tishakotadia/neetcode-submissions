class Solution:

    def encode(self, strs: List[str]) -> str:
        n=len(strs)
        s=[]
        for i in strs:
            l=len(i)
            s.append(str(l))
            s.append("#")
            s.append(i)
        return "".join(s)

    def decode(self, s: str) -> List[str]:
        n=len(s)
        l=[]
        i=0
        while i < n:
            j=i
            while s[j] != "#":
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            l.append(s[i:j])
            i=j
        return l


        