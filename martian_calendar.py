class Solution:
    def martian_calendar(self, days, k):
        hours = []
        for day in days:
            for i in range(day):
                hours.append(i + 1)
        
        max_sum = 0
        for i in range(len(hours) - k + 1):
            cur_sum = sum(hours[i : i + k])
            if cur_sum > max_sum:
                max_sum = cur_sum
        return max_sum

days = [1, 3, 2]
k = 4
sol = Solution()
print(sol.martian_calendar(days, k)) # 8
