class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count=1
        maxc=1
        ls=sorted(set(nums))
        n=len(ls)
        if n==0:
            return 0

        for i in range(n-1):
            if ls[i+1]==ls[i]+1:
                count+=1
            else:
                maxc=max(maxc, count)
                count=1
        maxc=max(maxc, count)
        return maxc
