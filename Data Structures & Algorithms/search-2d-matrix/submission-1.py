class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=len(matrix)
        c=len(matrix[0])
        num=0
        for i in range(r):
            if target>matrix[i][c-1]:
                continue
            else:
                num=i
                break
        for j in range(c):
            if target==matrix[num][j]:
                return True
        return False
