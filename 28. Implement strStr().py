class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if haystack is None or needle is None:
            return -1
        
        haystack_len = len(haystack)
        needle_len = len(needle)
        for i in range(haystack_len - needle_len + 1):
            if haystack[i:i+needle_len] == needle:
                return i
        return -1