import collections

class Solution:
    def countComponents(self, n):
        t = int(input('Please input a number: '))
        records = []
        for i in range(t):
            m = int(input("m:"))
            pairs = []
            for i in range(m):
                userinput = input()
                pairs.append([int(userinput.split(' ')[0]), int(userinput.split(' ')[1])])
            records.append(pairs)
        for edges in records:
            print(self.max_users(edges))
    
    def max_users(self, edges):             
        graph = collections.defaultdict(list)
        nodes = set()
        for n1, n2 in edges:
            graph[n1] += [n2]
            graph[n2] += [n1]
            nodes.add(n1)
            nodes.add(n2)

        visited = set()
        max_cnt = 0
        for node in nodes:
            if node not in visited:
                count = self.dfs(node, graph, visited)
            if count > max_cnt:
                max_cnt = count
        return(max_cnt)
    
    def dfs(self, start, graph, visited):
        if not graph[start] or start in visited:
            return 0 
        visited.add(start)
        for n in graph[start]:
            count = 1 + self.dfs(n, graph, visited)
        return count

sol = Solution()
sol.countComponents(2)