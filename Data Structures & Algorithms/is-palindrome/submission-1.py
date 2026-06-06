class Solution:
    def isPalindrome(self, s: str) -> bool:
        stri = ""
        for i in range(len(s)):
            if s[i].isalnum():
                stri+=s[i].lower()
        if stri==stri[::-1]:
            return True
        return False
