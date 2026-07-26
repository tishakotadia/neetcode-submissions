class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)

        while l<r:
            mid=l+((r-l)//2)
            req_days=1
            cur_weight=0
            
            for w in weights:
                if cur_weight+w>mid:
                    req_days+=1
                    cur_weight=0
                cur_weight+=w
            
            if req_days<=days:
                r=mid
            else:
                l=mid+1
        return l