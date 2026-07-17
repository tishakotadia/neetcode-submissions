class Solution:
    def mySqrt(self, x: int) -> int:
        div=x//2
        for i in range(div+1):
            pro=i*i
            if pro==x:
                return i
            elif pro>x:
                return i-1
        return div+1