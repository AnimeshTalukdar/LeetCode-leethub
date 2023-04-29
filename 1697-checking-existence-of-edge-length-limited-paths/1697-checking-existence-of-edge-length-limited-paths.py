from typing import List

class Solution:
    def distanceLimitedPathsExist(self, n: int, edge_list: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Define find function
        def find(node: int, parent: List[int]) -> int:
            if parent[node] != node:
                parent[node] = find(parent[node], parent)
            return parent[node]
        
        # Sort edge list and queries by weight/limit
        edge_list.sort(key=lambda x: x[2])
        queries = [(i, p, q, limit) for i, (p, q, limit) in enumerate(queries)]
        queries.sort(key=lambda x: x[3])
        
        # Initialize parent and rank lists
        parent = [i for i in range(n)]
        rank = [0] * n
        
        # Define union function
        def union(node1: int, node2: int, parent: List[int], rank: List[int]) -> bool:
            group1 = find(node1, parent)
            group2 = find(node2, parent)
            
            # If they are already in the same group, return False
            if group1 == group2:
                return False
            
            # Merge smaller group into the larger group
            if rank[group1] > rank[group2]:
                parent[group2] = group1
            elif rank[group1] < rank[group2]:
                parent[group1] = group2
            else:
                parent[group1] = group2
                rank[group2] += 1
            
            return True
        
        # Initialize answer list
        answer = [False] * len(queries)
        
        # Iterate over queries and edges
        edge_index = 0
        for i, p, q, limit in queries:
            # Add all edges that are within the limit to the union-find structure
            while edge_index < len(edge_list) and edge_list[edge_index][2] < limit:
                union(edge_list[edge_index][0], edge_list[edge_index][1], parent, rank)
                edge_index += 1
            
            # Check if p and q are connected
            if find(p, parent) == find(q, parent):
                answer[i] = True
        
        return answer
