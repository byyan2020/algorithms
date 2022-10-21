"""
We are working on a security system for a badged-access room in our company's building.
1. Given an ordered list of employees who used their badge to enter or exit the room, write a
function that returns two collections:
a. All employees who didn't use their badge while exiting the room - they recorded an enter
without a matching exit.
b. All employees who didn't use their badge while entering the room - they recorded an exit
without a matching enter.

exit = -1, enter = 1;
badge_records = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"]
]

find_mismatched_entries(badge_records)
Expected output: ["Paul", "Curtis"], ["Martha"]
"""
import collections


class Solution:
    def badge1(self, records):
        status = collections.defaultdict(list)
        for name, record in records:
            if status[name] == [] or record == 'enter':
                status[name].append(record)
            elif record == 'exit' and status[name][-1] == 'enter':
                status[name].pop()
        no_enter = []
        no_exit = []
        for name, record in status.items():
            if "enter" in record:
                no_exit += [name]
            if 'exit' in record:
                no_enter += [name]
        return no_exit, no_enter

sol = Solution()
badge_records = [
["Martha", "exit"],
["Paul", "enter"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "enter"],
["Paul", "enter"],
["Curtis", "enter"],
["Paul", "exit"],
["Martha", "enter"],
["Martha", "exit"],
["Jennifer", "exit"]
]
print(sol.badge1(badge_records))