class Solution:
    def productExceptSelf(self, nums):
        output = [] 
        for i in range(len(nums)):
            output1 = nums[:i]
            print(output1)
            output2 = nums[i+1:]
            print(output2)
            outputfinal = output1.append(output2)
            print(outputfinal)
            output.append(outputfinal)

        print(output)


obj = Solution()
obj.productExceptSelf([1,2,3,4])



