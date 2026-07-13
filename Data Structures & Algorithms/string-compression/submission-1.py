class Solution:
    def compress(self, chars: List[str]) -> int:
        writeIdx = 0
        n = len(chars)

        i = 0
        while i < n:
            char = chars[i]
            charStartIdx  = i

            while i < n and chars[i] == char:
                i += 1


            chars[writeIdx] = char
            writeIdx += 1

            freqCount = i - charStartIdx
            if freqCount > 1:
                for digit in str(freqCount):
                    chars[writeIdx] = digit
                    writeIdx += 1
            else:
                continue
        
        print(chars)
        return writeIdx