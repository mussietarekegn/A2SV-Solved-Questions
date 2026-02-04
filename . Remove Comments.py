class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        ans =[]
        flag=False
        curr =""

        for word in source:
            l=0
            while l<len(word):
                if not flag and l+1<len(word) and word[l]=='/' and word[l+1]=='*':
                    flag=True
                    l+=2
                elif flag and l+1<len(word) and word[l]=='*' and word[l+1]=='/':
                    flag=False
                    l+=2
                elif not flag and l+1<len(word) and word[l]=='/' and word[l+1]=='/':
                    break
                else:
                    if not flag:
                        curr+=word[l]
                    l+=1

            if not flag and curr:
                ans.append(curr)
                curr=""
 
        return ans


        
