class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows = len(matrix)
        cols = len(matrix[0])

        l, r = 0, rows*cols - 1

        while l<r:

            m = l + ((r-l)//2)

            x, y = m//cols, m%cols

            if target <= matrix[x][y]:
                r = m

            elif target > matrix[x][y]:
                l = m + 1

        return True if l <= rows*cols - 1 and matrix[l//cols][l%cols] == target else False