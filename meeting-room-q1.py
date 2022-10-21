# 第⼀题：类似meeting rooms，输⼊是⼀个int[][] meetings, int start, int end, 每个数都是时间，13：00
# =》 1300， 9：30 =》 18930， 看新的meeting 能不能安排到meetings
# ex: {[1300, 1500], [930, 1200],[830, 845]}, 新的meeting[820, 830], return true; [1450, 1500] return
# false;

class Solution:
    def meeting_room(self, meetings, new_meeting):
        meetings = sorted(meetings, key=lambda meeting: meeting[0])
        for i in range(len(meetings)):
            if new_meeting[1] <= meetings[i][0]:
                if i - 1 < 0:
                    return True
                if new_meeting[0] >= meetings[i-1][1]:
                    return True
        return False


# 第⼆题：类似merge interval，唯⼀的区别是输出，输出空闲的时间段，merge完后，再把两两个之间的空的输出就好，注意要加上0 - 第⼀个的start time.

    def sparetime(self, meetings):
        meetings.sort()
        merged = []
        for meeting in meetings:
            if not merged or meeting[0] > merged[-1][1]:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])

        res = []
        for i in range(len(merged)):
            if i == 0 and merged[i][0] != 0:
                res.append([0, merged[i][0]])
            else:
                res.append([merged[i - 1][1], merged[i][0]])
        return res
            
        

sol = Solution()
meetings = [[1300, 1500], [800, 1200], [830, 845]]
new_meeting1 = [820, 830]
new_meeting2 = [1450, 1500]
print(sol.meeting_room(meetings, new_meeting2))

print(sol.sparetime(meetings))
