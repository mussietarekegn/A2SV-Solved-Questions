class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapp={}

        for path in paths:
            part=path.split()
            directory=part[0]

            for p in part[1:]:
                name,left=p.split("(")
                content=left[:-1]
                full_path=directory+"/"+name
                if content not in mapp:
                    mapp[content]=[]
                mapp[content].append(full_path)
        ans=[]
        for values in mapp.values():
            if len(values)>1:
                ans.append(values)
        
        return ans
