class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = "".join(char.lower() for char in s if char.isalnum())
        for i in range(len(clean) // 2):
            if clean[i] != clean[-i-1]:
                return False
        return True
