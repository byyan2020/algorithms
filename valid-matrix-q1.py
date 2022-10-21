# 给⼀个N*N的矩阵，判定是否是有效的矩阵。有效矩阵的定义是每⼀⾏或者每⼀列的数字都必须正好是
# 1到N的数。输出⼀个bool。

class Solution(object):
    def valid_matrix(self, matrix):
        n = len(matrix)
        for i in range(n):
            row_set = set()
            col_set = set()
            for j in range(n):
                if matrix[i][j] in row_set or matrix[i][j] < 1 or matrix[i][j] > n:
                    return False
                row_set.add(matrix[i][j])

                if matrix[j][i] in col_set or matrix[j][i] < 1 or matrix[j][i] > n:
                    return False
                col_set.add(matrix[j][i])

        return True


sol = Solution()
matrix1 = [
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2]
]
matrix2 = [
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]
]
print(sol.valid_matrix(matrix1))
print(sol.valid_matrix(matrix2))
