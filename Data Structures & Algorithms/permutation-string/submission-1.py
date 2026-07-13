class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1FreqCount = [0] * 26
        s2FreqCount = [0] * 26

        lenS1, lenS2 = len(s1), len(s2)
        if lenS1 > lenS2:
            return False

        for i in range(lenS1):
            s1FreqCount[ord(s1[i]) - ord('a')] += 1
            s2FreqCount[ord(s2[i]) - ord('a')] += 1
        
        matchCount = 0
        for i in range(26):
            if s1FreqCount[i] == s2FreqCount[i]:
                matchCount += 1
        print(matchCount)
        

        l = 0 
        for r in range(lenS1, lenS2):
            if matchCount == 26:
                return True

            rightElementIndex = ord(s2[r]) - ord('a')
            s2FreqCount[rightElementIndex] += 1
            #If adding the count makes the count equal to that of S1Freq, then its a match
            if s2FreqCount[rightElementIndex] == s1FreqCount[rightElementIndex]:
                matchCount += 1
            #If the previous count was equal and ADDING made it not equal, then its not a match
            elif s2FreqCount[rightElementIndex] - 1 == s1FreqCount[rightElementIndex]:
                matchCount -= 1
            

            leftElementIndex = ord(s2[l]) - ord('a')
            s2FreqCount[leftElementIndex] -= 1
            #If removal made the count equal [we fixed a mismatch], then its a match
            if s2FreqCount[leftElementIndex] == s1FreqCount[leftElementIndex]:
                matchCount += 1
            #If removal made the count inequal [we broke a match], then its not a match
            elif s2FreqCount[leftElementIndex] + 1 == s1FreqCount[leftElementIndex]:
                matchCount -= 1
            l+=1
        

        return matchCount == 26
