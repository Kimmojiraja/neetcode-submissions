class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # taking the input
        left = 0 
        max_length = 0 
        char_set = set()
    # rhe left and right moving logic 
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1      # move one step forward 
            char_set.add(s[right])
            max_length = max(max_length,right-left+1)
        return max_length

            
        