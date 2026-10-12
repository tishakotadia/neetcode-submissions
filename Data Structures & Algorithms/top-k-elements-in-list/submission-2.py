class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort is best, maxheap is better, sort is good. all use hash map.

        count={}
        for i in nums:
                count[i]=1+count.get(i, 0)
        
        ls=[[] for i in range(len(nums)+1)]

        for num, freq in count.items():
            ls[freq].append(num)

        res=[]
        for i in range(len(ls)-1, 0, -1):
            for j in ls[i]:
                res.append(j)
                if len(res)==k:
                    return res


