# 48. Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

from typing import List


class Solution:

    # 2022/01/18 Scott
    # Time Complexity: O(n^2) 99.54%
    # Space Complexity: O(n) 45.82%
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        c = n - 2
        if n == 2:
            c += 1
        for j in range(c):
            left = [matrix[j][i] for i in range(j, n - j)]
            # First row to the right side
            for i in range(j, n - j):
                left[i - j], matrix[i][n - 1 - j] = matrix[i][n - 1 - j], left[i - j]
                
            # Previously right side to bottom
            for i in range(j, n - 1 - j):
                left[i + 1 - j], matrix[n - 1 - j][-i - 2] = matrix[n - 1 - j][-i - 2], left[i + 1 - j]
            
            # Previously bottom to the left side
            for i in range(j, n - 1 - j):
                left[i + 1 - j], matrix[-i - 2][j] = matrix[-i - 2][j], left[i + 1 - j]

            # Previously left to top
            for i in range(j, n - 1 - j):
                left[i + 1 - j], matrix[j][i + 1] = matrix[j][i + 1], left[i + 1 - j]
        

if __name__ == '__main__':
    s = Solution()
    
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    s.rotate(matrix)
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotate(matrix)
    matrix = [[1,2],[3,4]]
    s.rotate(matrix)
            
