class Solution:
    def verify(self, str1, str2, gcd):
        result1, result2 = "", ""
        if (len(str1) % len(gcd) != 0) and (len(str2) % len(gcd) != 0):
            return False
        else:
            for i in range(len(str1)//len(gcd)):
                result1 += gcd
            for i in range(len(str2)//len(gcd)):
                result2 += gcd

            if result1 == str1 and result2 == str2:
                return True
            else:
                return False

    def gcdOfStrings(self, str1, str2):
        gcd = ""
        truegcd = ""
        if len(str1) > len(str2):
            small = str2
        else:
            small = str1

        for char in small:
            gcd += char
            if self.verify(str1, str2, gcd):
                truegcd = gcd
            else:
                continue

        return truegcd


obj = Solution()
print(obj.gcdOfStrings("ABABAB", "ABAB"))







