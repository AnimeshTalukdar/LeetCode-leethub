class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        color = {}
        curcolor=False
        queue=[]
        visited={}

        def fun(k):
            queue.append(k)
            color[k]=False
            while queue!=[]:
                cur = queue.pop(0)
                visited[cur]=True
                nextcolor = not color[cur]
                for adj in graph[cur]:
                    if adj not in visited:
                        color[adj]=nextcolor
                        queue.append(adj)

        for i in range(len(graph)):
            if i not in color:
                fun(i)
            for j in range(len(graph[i])):
                if color[graph[i][j]]==color[i]:
                    return False

        return True
                            
        