"""
2. We want to find employees who badged into our secured room unusually often. We have an
unordered list of names and access times over a single day. Access times are given as three or
four-digit numbers using 24-hour time, such as "800" or "2250".
Write a function that finds anyone who badged into the room 3 or more times in a 1-hour
period, and returns each time that they badged in during that period. (If there are multiple 1-
hour periods where this was true, just return the first one.)

badge_records = [
["Paul", 1315],
["Jennifer", 1910],
["John", 830],
["Paul", 1355],
["John", 835],
["Paul", 1405],
["Paul", 1630],
["John", 855],
["John", 915],
["John", 930],
["Jennifer", 1335],
["Jennifer", 730],
["John", 1630],]

Expected output:
{"John": [830, 835, 855, 915, 930]
"Paul": [1315, 1355, 1405]}
"""


class Solution:
    def badge2(self, records):
        dict = {}
        for name, time in records:
            dict[name] = dict.get(name, []) + [time]

        unusual = {}
        for name, time in dict.items():
            time.sort()
            if len(time) < 3:
                continue
            for i in range(len(time) - 2):
                j = i + 2
                while j < len(time) and time[j] - time[i] <= 100:
                    j += 1
                    unusual[name] = time[i:j]
                if name in unusual:
                    break
        return unusual


sol = Solution()
badge_records1 = [
    ["Paul", 1315],
    ["Jennifer", 1910],
    ["John", 830],
    ["Paul", 1355],
    ["John", 835],
    ["Paul", 1405],
    ["Paul", 1630],
    ["John", 855],
    ["John", 915],
    ["John", 930],
    ["Jennifer", 1335],
    ["Jennifer", 730],
    ["John", 1630], ]

print(sol.badge2(badge_records1))
