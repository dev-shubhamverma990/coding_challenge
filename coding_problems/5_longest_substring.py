"""
Check the longest String with no repeating characters.
"""


# def longest_substring(s: str) -> int:
#     char_index = {}
#     longest = 0
#     start = 0

#     for end, char in enumerate(s):
#         if char in char_index and char_index[char] >= start:
#             start = char_index[char] + 1
#         char_index[char] = end
#         longest = max(longest, end - start + 1)

#     return longest


def longest_substring_brute_force(s: str) -> int:
    longest = 0
    for i in range(len(s)):
        seen = set()
        for j in range(i, len(s)):
            if s[j] in seen:
                break
            seen.add(s[j])
        longest = max(longest, len(seen))
    return longest
