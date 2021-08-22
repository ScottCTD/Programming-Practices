# You are given a rows x cols matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.
# Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (rows - 1, cols - 1),
# find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.
# Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative return -1.
# Notice that the modulo is performed after getting the maximum product.
# Scott 2021/08/12

class Solution:

    # Original
    # Correct but slow
    # Need to learn more to do it
    def maxProductPath(self, grid: list[list[int]]) -> int:
        max_product = [-1]
        row_len = len(grid[0])
        column_len = len(grid)

        def func(row: int, column: int, product: int):
            product *= grid[column][row]
            # Reach the end
            if row == row_len - 1 and column == column_len - 1:
                max_product[0] = max(max_product[0], product)
                return
            # Turn right if it could
            if row < row_len - 1:
                func(row + 1, column, product)
            # Turn left if it could
            if column < column_len - 1:
                func(row, column + 1, product)
            return

        func(0, 0, 1)
        if max_product[0] < 0:
            return -1
        else:
            return max_product[0] % (10 ** 9 + 7)


if __name__ == '__main__':
    print(Solution().maxProductPath([
        [-1, -2, -3],
        [-2, -3, -3],
        [-3, -3, -2]]) == -1)
    print(Solution().maxProductPath([
        [1, -2, 1],
        [1, -2, 1],
        [3, -4, 1]]) == 8)
    print(Solution().maxProductPath(
        [[1, 3],
         [0, -4]]) == 0)
    print(Solution().maxProductPath([
        [1, 4, 4, 0],
        [-2, 0, 0, 1],
        [1, -1, 1, 1]]) == 2)
