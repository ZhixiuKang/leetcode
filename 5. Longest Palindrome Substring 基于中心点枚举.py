class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        self.start, self.longest = 0, 0
        for middle in range(len(s)):
            self.find_longest_palindrome_from(s, middle, middle)
            self.find_longest_palindrome_from(s, middle, middle + 1)
            
        return s[self.start:self.start+self.longest]
            
    def find_longest_palindrome_from(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        if self.longest < right - left - 1:
            self.longest = right - left - 1
            self.start = left + 1