class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        r=Counter(answers)
        sum=0
        for i in range(len(answers)):
            if answers[i] in r:
                sum+=answers[i]+1
                r[answers[i]]-=min(r[answers[i]], answers[i]+1)
                if r[answers[i]]<=0:
                    r.pop(answers[i])
        return sum