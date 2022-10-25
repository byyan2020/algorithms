"""
Imagine there are n points along a straight trail, while a runner run sprints of intervals between those point.
The training plan is an array a[], which implies the runner should run from point a[i] to point a[i+1].

For example, given n = 10, a = [2, 4, 1, 2].
The runner should run from point 2 to point 4,
then turn back from point 4 to point 1,
and then from point 1 to point 2.

Find the point that visited the most by runner after he finished training, i.e. in above example, point 2 is the most visited.
If more than one point are visited the most, find the point with minimum index.
"""

# record start and end of each pair
# accumulate sum to get the frequency of visits

def getmostvisited(n, sprints):
    records = [0] * (n + 2)
    for i in range(len(sprints) - 1):
        start = min(sprints[i], sprints[i + 1])
        end = max(sprints[i], sprints[i + 1])
        records[start] += 1
        records[end + 1] -= 1

    cur = 0
    max_visited = 0
    ans = 0
    for i in range(1, n + 1):
        records[i] += cur
        cur = records[i]
        if cur > max_visited:
            max_visited = cur
            ans = i

    return ans

n = 10
a = [2, 4, 1, 2]
ans = getmostvisited(n, a)
print(ans)
    
