"""
输入是int[][] input, input[0]是input[1] 的parent，比如 {{1,4}, {1,5}, {2,5}, {3,6}, {6,7}}会形成上面的图
第一问是只有0个parents和只有1个parent的节点

  1    2    3
/  \  /      \
4    5        6
                \
                  7

"""


import collections


class Solution:
    def find_parent(self, input_list):
        parents = {}
        res = []
        for par, child in input_list:
            parents[child] = parents.get(child, 0) + 1
            parents[par] = parents.get(par, 0)
        for node, count in parents.items():
            if count <= 1:
                res.append(node)
        return res

# 第⼆问是 两个指定的点有没有公共祖先 (Time: O(N) , Space: O(N) )
    def ancestors(self, input_list, n1, n2):
        # build the mapping from child to parents
        children = {}
        for par, child in input_list:
            children[child] = children.get(child, []) + [par]

        print(children)

        def get_parents(node):
            # BFS get all parents
            queue = collections.deque([node])
            parent = set()
            while queue:
                n = queue.popleft()
                if n not in children:
                    continue
                for par in children[n]:
                    if par in parent:
                        continue
                    parent.add(par)
                    queue.append(par)
            return parent
        # use set intersect to get common ancestors
        return True if get_parents(n1) & get_parents(n2) else False


# 第三问是 就⼀个点的最远祖先，如果有好⼏个就只需要输出⼀个就好，举个栗⼦，这⾥5的最远祖先可以是1或者2，输出任意⼀个就可以
# (Time: O(N) , Space: O(N) )

    def furtheast_ancestor(self, input_list, node):
        children_map = {}
        for par, child in input_list:
            children_map[child] = children_map.get(child, []) + [par]
        distance = 0
        res = None
        queue = collections.deque([(node, 0)])
        while queue:
            cur_node, cur_d = queue.popleft()
            cur_d += 1
            if cur_d > distance:
                distance = cur_d
                res = cur_node
            if cur_node not in children_map: continue
            for next in children_map[cur_node]:
                queue.append((next, cur_d))
        return res

sol = Solution()
inputlist = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7], [9, 3], [10, 1], [11, 10], [11, 9]]
print(sol.find_parent(inputlist))  # [1,2,3,4,6,7]

print(sol.ancestors(inputlist, 1, 7))

print(sol.furtheast_ancestor(inputlist, 7))
