class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        mapp=defaultdict(int)

        for ch in chars:
            mapp[ch]+=1

        total_len=0

        for word in words:
            w_mapp=defaultdict(int)
            good=True
            for i in word:
                w_mapp[i]+=1

                if w_mapp[i]>mapp[i]:
                    good=False
                    break

            if good:
                total_len+=len(word)

        return total_len
