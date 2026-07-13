class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        word1Len, word2Len = len(word1), len(word2)

        # let dp[i] be the number of edits to make at idx 'i' for word1
        prevDP = [i for i in range(word2Len+1)]


        for i in range(1, word1Len+1):
            currDP = [0] * (word2Len+1)
            currDP[0] = i

            for j in range(1, word2Len+1):

                if word1[i-1] == word2[j-1]:
                    currDP[j] = prevDP[j-1]
                else:
                    # min(delete, insert, replace)
                    currDP[j] = 1 + min(prevDP[j], currDP[j-1], prevDP[j-1])
            
            prevDP = currDP
        

        return prevDP[word2Len]
