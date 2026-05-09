class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        s = s.casefold()

        for c in s:
            if c.isalnum():
                cleaned += c

        # return cleaned == cleaned[::-1]
        print(cleaned)
        left = 0
        right = len(cleaned)-1
        while left < right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
