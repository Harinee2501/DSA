class Solution(object):
    def validPath(self, n, edges, source, destination):
        adj={i:[] for i in range(n)}
        for i,j in edges:
            adj[i].append(j)
            adj[j].append(i)
        queue=deque([])
        visited=set()
        queue.append(source)
        visited.add(source)
        while queue:
            node=queue.popleft()
            if node==destination:
                return True
            for i in adj[node]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return False