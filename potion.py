import heapq
from types import new_class


class Solution:
    def potion(self, k, herbs):
        herbs.sort(reverse = True)
        heap = []
        res = 0

        i = 0
        while len(heap) <= k and i < len(herbs):
            if len(heap) < k:
                heapq.heappush(heap, herbs[i])
                i += 1
            if len(heap) == k:
                cur_potion = heapq.heappop(heap)
                res += cur_potion
                new_heap = []
                for _ in range(k - 1):
                    num = heapq.heappop(heap) - cur_potion
                    if num:
                        heapq.heappush(new_heap, num)
                heap = new_heap
        return res


k = 4
herbs1 = [4, 4, 4, 4, 4] # 4
herbs2 = [1, 2, 3, 5] # 3
herbs3 = [2, 2, 3, 5] # 3
sol = Solution()
print(sol.potion(k, herbs1))
print(sol.potion(k, herbs2))
print(sol.potion(k, herbs3))

