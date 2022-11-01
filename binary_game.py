class Solution:
    def binary_game(self, min_len, max_len, group0, group1):
        dp = [0] * (max_len + 1)
        dp[0] = 1
        for i in range(1, max_len + 1):
            temp = 0
            if i - group0 >= 0:
                temp += dp[i - group0] % 1000000007
            if i - group1 >= 0:
                temp += dp[i - group1] % 1000000007
            dp[i] = temp % 1000000007
        ans = 0
        for num in dp[min_len: max_len + 1]:
            ans += num
        return ans

sol = Solution()
min_len = 1
max_len = 30
group0 = 1
group1 = 2
print(sol.binary_game(min_len, max_len, group0, group1))