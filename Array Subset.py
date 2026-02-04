#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
       a.sort()
       b.sort()
       count=0
       j=0
       
       for i in range(len(b)):
            while j<len(a):
                if b[i]==a[j]:
                    count+=1
                    j+=1
                    break
                j+=1
            
                

                
       if count==len(b):
            return True
       else:
            return False
        
    
    
    
