class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word=s.split()

        if len(pattern)!=len(word):
            return False
        
        patt={}
        wo={}

        for p,w in zip(pattern,word):
            if p in patt:
                if patt[p]!=w:
                    return False
            else:
                patt[p]=w
            
            if w in wo:
                if wo[w]!=p:
                    return False
            else:
                wo[w]=p

        return True

