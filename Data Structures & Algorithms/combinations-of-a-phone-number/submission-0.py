class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        
        res = []

        def dfs(idx, path):
            if idx == len(digits):
                res.append(''.join(path))
                return
            
            currDigit = digits[idx]
            choices = digitToChar[currDigit]

            for ch in choices:
                path.append(ch)
                dfs(idx+1, path)
                path.pop()

        dfs(0,[])
        return res
