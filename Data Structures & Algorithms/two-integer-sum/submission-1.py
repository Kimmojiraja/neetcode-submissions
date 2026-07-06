class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ok let's do it tt

        # here the idea is about storing as hash to access the index

        seen = {} # which store key and value

        for i in range(len(nums)):

            needed  = target - nums[i] 

            if needed in seen:
                return [seen[needed],i]
            seen[nums[i]] = i # i think it will automatically adds to dicttt may be



        