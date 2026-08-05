class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        result = []
        for j in range(len(nums)):
            product = 1

            for i in range(len(nums)):
                if i != j:
                    product *= nums[i]

            result.append(product)
        return result
