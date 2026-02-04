class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a)!=len(b):
            return False
        
        else:
            a.sort()
            b.sort()
            for i in range(len(a)):
                if a[i]==b[i]:
                    continue
                else:
                    return False
            return True
