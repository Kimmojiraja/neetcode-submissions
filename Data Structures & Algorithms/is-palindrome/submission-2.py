class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum(): # VALIDATING FOR EACH CHAR IS ALPHANUMBEICS
                newstr += c.lower()
        return newstr == newstr[::-1]
