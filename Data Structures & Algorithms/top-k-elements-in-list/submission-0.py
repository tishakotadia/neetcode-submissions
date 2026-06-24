class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int)
        for i in nums:
            dic[i]+=1
        
        arr=[]
        for num, count in dic.items():
            arr.append([count, num])
        arr.sort()

        res=[]
        while k>0:
            res.append(arr.pop()[1])
            k-=1
        return res

