class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result


obj = Solution()
print(obj.kidsWithCandies([2, 3, 5, 1, 3], 3))
