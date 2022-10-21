""" 
there is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.
for the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s. The rectangles are separated by 1s. Find all the rectangles.
EXAMPLE：
input:
[
[1,1,1,1,1,1],
[0,0,1,0,1,1],
[0,0,1,0,1,0],
[1,1,1,0,1,0],
[1,0,0,1,1,1]
]
output:
[
[1,0,2,1],
[1,3,3,3],
[2,5,3,5],
[4,1,4,2]
]
"""


class Solution:
    def find_rectangles(self, grid):
        if not grid or not grid[0]:
            return []

        def locate_rec(i, j):
            init_i, init_j = i, j
            while i < len(grid) and grid[i][j] == 0:
                i += 1
            while j < len(grid[0]) and grid[i - 1][j] == 0:
                j += 1

            for x in range(init_i, i):
                for y in range(init_j, j):
                    grid[x][y] = -1
            return [init_i, init_j, i - 1, j - 1]

        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    res.append(locate_rec(i, j))
        return res


sol = Solution()
input = [
    [1, 1, 1, 1, 1, 1],
    [0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1, 0],
    [1, 0, 0, 1, 1, 1]
]
ans = sol.find_rectangles(input)
print(ans)
