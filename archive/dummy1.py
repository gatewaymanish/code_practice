# gemini solutions
#Problem: Length of the Longest Substring Without Repeating Characters

# Given a string s, return the length of the longest substring without repeating characters.

# Examples
#
#
# s = "abcabcbb" → 3 # abc
#
# s = "bbbbb" → 1 # b
#
# s = "pwwkew" → 3 # kew
#
# s = "" → 0


def longest_sub(s):
    n = len(s)
    if n == 0:
        return 0
    longest_substring = 0

    for i in range(n):
        sub = s[i]
        for j in range(i+1, n):
            if s[j] not in sub:
                sub += s[j]
                # print('Debug: sub: ', sub)
            else:
                longest_substring = max(longest_substring, len(sub))
                # print('Debug: longest: ', longest_substring)
                break
    return longest_substring


# s = "abcabcbb"
s = "pwwkew"
# print(longest_sub(s))


def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

# Example usage
print(lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(lengthOfLongestSubstring("bbbbb"))     # Output: 1
print(lengthOfLongestSubstring("pwwkew"))    # Output: 3
