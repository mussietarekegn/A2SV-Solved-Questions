class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
            mapp={}
            ans=[]

            if len(list1)>=len(list2):
                
                for i in range(len(list1)):
                    for j in range(len(list2)):
                        if list1[i]==list2[j]:
                            key=list1[i]
                            mapp[key]=i+j

                if len(mapp)==1:
                    return list(mapp.keys())

                val=float("inf")

                for values in mapp.values():
                    val=min(val,values)
                
                for keys,values in mapp.items():
                    if values==val:
                        ans.append(keys)
                
                return ans
            else:
                for i in range(len(list2)):
                    for j in range(len(list1)):
                        if list2[i]==list1[j]:
                            key=list2[i]
                            mapp[key]=i+j
                if len(mapp)==1:
                    return list(mapp.keys())

                val=float("inf")

                for values in mapp.values():
                    val=min(val,values)
                
                for keys,values in mapp.items():
                    if values==val:
                        ans.append(keys)
                
                return ans
            
            
