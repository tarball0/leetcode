import re

class Solution:
    def reverseWords(self, s):
        output = ""
        s = re.sub(r" +", " ", s)
        s = s.strip()
        s = s.split(" ")
        s = s[::-1]
        for i in range(len(s)):
            output += s[i]
            if i != (len(s) - 1):
                output += ' '

        return output

