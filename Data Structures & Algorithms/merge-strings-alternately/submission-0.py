class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1, len2 = len(word1), len(word2)
        ptr1 = ptr2 = 0
        res = []

        while ptr1 < len1 and ptr2 < len2:
            res.append(word1[ptr1])
            res.append(word2[ptr2])

            ptr1 += 1
            ptr2 += 1
        
        if len1 == len2:
            return "".join(res)
        elif ptr1 == len1:
            return "".join(res) + word2[ptr2:]
        else:
            return "".join(res) + word1[ptr1:]