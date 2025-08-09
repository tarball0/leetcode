class Solution:
    def reverseVowels(self, s):
        indexarr = []
        vowelarr = []

        for i in range(len(s)):
            if s[i] in "aeiouAEIOU":
                indexarr.append(i)
                vowelarr.append(s[i])

        vowelarr = vowelarr[::-1]
        j = 0

        for i in indexarr:
            s = s[:i] + vowelarr[j] + s[i+1:]
            j += 1

        return s
