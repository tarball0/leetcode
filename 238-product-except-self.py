class Solution:
    def productExceptSelf(self, nums):
        answer = []
        lprod = 1
        larr = [1]
        
        for i in range(len(nums)-1):
            lprod *= nums[i]
            larr.append(lprod)

        rprod = 1
        rarr = []
        var = 1

        for i in range(len(nums)):
            rarr.append(None)

        rarr[len(nums)-1] = 1
        for i in range((len(nums)-2), -1, -1):
            rprod *= nums[i+1]
            rarr[i] = rprod

        for i in range(len(nums)):
            answer.append(larr[i] * rarr[i])

        return answer




obj = Solution()
obj.productExceptSelf([1, 2, 3, 4])



