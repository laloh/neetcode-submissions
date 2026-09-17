class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj_list = defaultdict(list) 
        for src, dest in edges:
            adj_list[src].append(dest)
            adj_list[dest].append(src)
        
        queue = deque([(0, -1)])
        visited = {0}
        
        while queue:
            node, parent = queue.popleft()
           
            for adj in adj_list[node]:
                if adj == parent:
                    continue
                if adj in visited:
                    return False
                
                queue.append((adj, node))
                visited.add(adj)

        print(visited)        
        print(edges)        
        return len(visited) == n

