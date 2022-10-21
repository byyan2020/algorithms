# 给每个user访问历史记录，找出两个user之间longest continuous common history
# 输⼊： [
# ["3234.html", "xys.html", "7hsaa.html"], // user1
# ["3234.html", ''sdhsfjdsh.html", "xys.html", "7hsaa.html"] // user2
# ], user1 and user2 （指定两个user求intersect）
# 输出：["xys.html", "7hsaa.html"]

class Solution:
    def LCS(self, user1, user2):
        n, m = len(user1), len(user2)
        maxlen = 0
        lst_history = []
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                return
