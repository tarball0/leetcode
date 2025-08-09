class Solution:
    def mergeAlternately(self, word1, word2):
        retword = ""

        if len(word1) > len(word2):
            greater = word1
            lesser = len(word2)
        else:
            greater = word2
            lesser = len(word1)

        i = 0

        for i in range(lesser):
            retword += word1[i]
            retword += word2[i]

        for j in range(i + 1, len(greater)):
            retword += greater[j]

        return retword


obj = Solution()
print(obj.mergeAlternately("ab", "pqrs"))
