class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        maps=Counter(s)
        mapt=Counter(t)
        
        for letter in maps:
            if letter in mapt:
                if maps[letter]!=mapt[letter]:
                    return False
            else:
                return False
        
        return True and len(s)==len(t)
