class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])-1
        num=0
        for i in range(r):
            if target>matrix[i][c]:
                continue
            else:
                num=i
                break
        left=0
        right=c
        while left<=right:
            mid=left+(right-left)//2
            if target==matrix[num][mid]:
                return True
            elif target>matrix[num][mid]:
                left=mid+1
            else:
                right=mid-1
        return False
