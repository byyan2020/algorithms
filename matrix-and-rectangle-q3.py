"""
there is an image filled with 0s and 1s. There is at most one rectangle in this image filled with 0s, find the rectangle. Output could be the coordinates of top-left and bottom-right elements of the rectangle, or top-left element, width and height.

for the same image, it is filled with 0s and 1s. It may have multiple rectangles filled with 0s. The rectangles are separated by 1s. Find all the rectangles.

the image has random shapes filled with 0s, separated by 1s. Find all the shapes. Each shape is represented by coordinates of all the elements inside.

Input: grid = [
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,1,0,0],
[0,0,0,1,1]
]
"""


class Solution:
    def find_shapes(self, grid):
        if not grid or not grid[0]:
            return []

        res = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    path = []
                    self.dfs(grid, i, j, path)
                    res.append(path)
        return res

    def dfs(self, grid, i, j, path):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return
        if grid[i][j] == 1:
            return
        path.append([i, j])
        grid[i][j] = 1
        self.dfs(grid, i + 1, j, path)
        self.dfs(grid, i - 1, j, path)
        self.dfs(grid, i, j + 1, path)
        self.dfs(grid, i, j - 1, path)


sol = Solution()
input = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]]
ans = sol.find_shapes(input)
print(ans)
