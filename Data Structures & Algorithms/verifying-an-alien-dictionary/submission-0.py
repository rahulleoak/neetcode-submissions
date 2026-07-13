class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charToIdx = { ch : i for i, ch in enumerate(order) }

        for j in range(len(words) - 1):
            word1, word2 = words[j], words[j+1]

            for i in range(len(word1)):
                if i == len(word2):
                    return False

                ch1 = word1[i]
                ch2 = word2[i] 
                
                if ch1 != ch2:
                    if charToIdx[ch1] > charToIdx[ch2]:
                        return False # Invalid ordering since ch1 > ch2
                    break # Valid ordering since ch1 < ch2
        
        return True