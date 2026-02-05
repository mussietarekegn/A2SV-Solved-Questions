class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapp=defaultdict(int)
        domains=[]

        for c in cpdomains:
            part=c.split()
            count=int(part[0])
            domains.append(part[1])

            for j in range(len(part[1])-1,-1,-1):
                if part[1][j]==".":
                    domains.append(part[1][j+1:])
                    mapp[part[1][j+1:]]+=count
        
            mapp[part[1]]+=count


        return [f"{val} {key}" for key,val in mapp.items()]
