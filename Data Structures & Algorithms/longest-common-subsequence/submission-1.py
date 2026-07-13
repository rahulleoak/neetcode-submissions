class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        m, n = len(text1), len(text2)
        prevState = [0] * (n+1)

        for i in range(1, m+1):
            currState = [0] * (n+1)

            for j in range(1, n+1):
                # Match: Diagonal
                if text1[i-1] == text2[j-1]:
                    currState[j] = 1 + prevState[j-1]

                # Mismatch: Max of TOP or LEFT
                else:
                    currState[j] = max(prevState[j], currState[j-1])

            prevState = currState
        
        return prevState[n]
                
        