class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r=1,max(piles)
        res=r

        while l<=r:
            mid=l+((r-l)//2)

            totTime=0
            for p in piles:
                totTime+=math.ceil(p/mid)
            if totTime<=h:
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res