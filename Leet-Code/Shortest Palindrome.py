class Solution(object):
    def shortestPalindrome(self, s):
        prefix_idx = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == s[prefix_idx]:
                prefix_idx += 1

        if prefix_idx == len(s):
            return s

        suffix = s[prefix_idx:]
        return suffix[::-1] + self.shortestPalindrome(s[:prefix_idx]) + suffix
