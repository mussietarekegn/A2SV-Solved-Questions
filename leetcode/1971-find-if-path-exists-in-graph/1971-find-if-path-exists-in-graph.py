class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit=set()

        def check(node):
            if node==destination:
                return True
                
            visit.add(node)

            for n in graph[node]:
                if n not in visit:
                    if check(n):
                        return True
            return False

        return check(source)
            
