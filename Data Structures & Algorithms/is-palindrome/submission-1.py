class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char.lower()for char in s if char.isalnum())
        j = len(s)-1
        for i in range(len(s)//2):
            if s[i] == s[j]:
                    j = j - 1
                    # continue
            else: 
                return False
        return True
                

