class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * (len(nums))
        # now let us gof or the left and righ approach 
        prefix = 1
        for i in range(len(nums)):
            # this loop for the prefix 
            result[i]= prefix 
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1 , -1,-1):
            result[i] *= postfix
            postfix *= nums[i]

        return result
