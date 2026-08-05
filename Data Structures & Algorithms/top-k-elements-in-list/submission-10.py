class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter_ = {}
        for num in nums:
            counter_[num] = counter_.get(num,0) + 1
        sorted_items = sorted(counter_.items(), key=lambda x: x[1], reverse=True)

        result = []
        for num,freq in sorted_items[:k]:
            result.append(num)
        return result