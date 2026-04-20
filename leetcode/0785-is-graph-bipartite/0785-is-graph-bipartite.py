class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n

        def check(node):
            for n in graph[node]:
                if color[n]==-1:
                    if color[node]==0:
                        color[n]=1
                    else:
                        color[n]=0
                    if not check(n):
                        return False
                
                elif color[n]==color[node]:
                    return False
            
            return True

        for i in range(n):
            if color[i]==-1:
                color[i]=0
                if not check(i):
                    return False
        
        return True