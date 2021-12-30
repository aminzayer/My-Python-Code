"""""
Given a string s, find the length of the longest substring without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.

"""""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = {}
        maximum_length = 0
        start = 0
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]] + 1)

            seen[s[end]] = end
            maximum_length = max(maximum_length, end-start + 1)
        return maximum_length

# Test Code
Sl = Solution()
print(Sl.lengthOfLongestSubstring("abcabcbb"))
print(Sl.lengthOfLongestSubstring("bbbbb"))
print(Sl.lengthOfLongestSubstring("pwwkew"))
