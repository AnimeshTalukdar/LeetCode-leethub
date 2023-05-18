class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        incoming = set()
        for edge in edges:
            incoming.add(edge[1])
        res = []
        for i in range(n):
            if i not in incoming:
                res.append(i)
        return res
    

        
