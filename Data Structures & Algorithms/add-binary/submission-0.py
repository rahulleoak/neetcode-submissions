class Solution:

    def add_to (self, carry, str_, elema, elemb):
        ans = str_
        carry_ = "0" 
        if (elema == "0" and elemb =="0"):
            if (carry =="0"):
                ans = "0" + ans
                carry_ = "0"
            if (carry == "1"):
                carry_ = "0"
                ans = "1" + ans

        if (elema == "1" and elemb =="0"):
            if (carry =="0"):
                ans = "1" + ans
                carry_ = "0"
            if (carry == "1"):
                ans = "0" + ans
                carry_ = "1"
        
        if (elema == "0" and elemb =="1"):
            if (carry =="0"):
                ans = "1" + ans
                carry_ = "0"
            if (carry == "1"):
                ans = "0" + ans
                carry_ = "1"

        if (elema == "1" and elemb =="1"):
            if (carry =="0"):
                ans = "0" + ans
                carry_ = "1"
            if (carry == "1"):
                ans = "1" + ans
                carry_ = "1"
        return carry_, ans
        

    def addBinary(self, a: str, b: str) -> str:
        
        l = max(len(a), len(b))
        if (len(a) < l):
            a = "0"*(l-len(a)) + a
        if (len(b) < l):
            b = "0"*(l-len(b)) + b

        print(a)
        print(b)

        ans = ""
        carry = "0"
        for i in reversed(range(l)):             
            elema = "0"
            elemb = "0"
            if (i < len(a)):
                elema = a[i]
            if (i < len(b)):
                elemb = b[i]

            print(elema, elemb)

            carry, ans = self.add_to(carry, ans, elema, elemb)

            print(carry, ans)
        if carry == "0": return ans
        return carry + ans