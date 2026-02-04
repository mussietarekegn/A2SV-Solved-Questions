class Solution:    
    def findUnion(self, a, b):
        # code here
        ab=set()
        
        for i in range(len(a)):
            ab.add(a[i])
        for i in range(len(b)):
            ab.add(b[i])
        
        return list(ab)
