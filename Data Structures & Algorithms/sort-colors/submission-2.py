class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        '''for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp'''
        # 1,0,1,2
        c0, c1, c2=0,0,0
        for i in nums:
            if i==0:
                c0+=1
            elif i==1:
                c1+=1
            else:
                c2+=1
        # c0 = 1 , c2 = 1, c1 =2 
        for i in range(0, len(nums)):
            if(c0!=0):
                nums[i] = 0
                c0-=1;
            elif (c1!=0):
                nums[i] = 1;
                c1-=1;
            else:
                nums[i] = 2;
                c2-=1;