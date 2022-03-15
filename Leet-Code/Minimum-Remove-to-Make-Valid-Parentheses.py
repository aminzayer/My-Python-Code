#Minimum Remove to Make Valid Parentheses
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

#     It is the empty string, contains only lowercase characters, or
#     It can be written as AB (A concatenated with B), where A and B are valid strings, or
#     It can be written as (A), where A is a valid string.

 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"

# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        s = list(s)
        for i in range(len(s)):
            c = s[i]
            if c == '(':
                st.append(i)
            elif c == ')':
                if len(st) == 0:
                    s[i] = '*'
                else:
                    st.pop()

        while len(st):
            s[st[-1]] = '*'
            st.pop()
        res = ''
        for c in s:
            if c != '*':
                res += c
        return res
 
