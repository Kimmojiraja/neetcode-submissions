class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        count_char = {}
        count_freq = 0 
        max_length = 0

        for right in range(len(s)):
                # finding the frequency of the charactes i mean count 
            count_character = s[right]
            count_char[count_character] = count_char.get(count_character,0) + 1

            count_freq =  max(count_freq , count_char[count_character])

            # now checking if it valid or not may be it has more then k
            if (right - left + 1) - count_freq > k :
                # shrinking the window
                
                count_char[s[left]] -= 1 
                left += 1 
            # now finally updating the finall max lenght in the whole thing 
            corrent_now = right - left + 1 
            max_length = max(max_length,corrent_now)
        return max_length
                    