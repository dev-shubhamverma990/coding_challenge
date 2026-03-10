"""
Check if two strings are anagrams.

An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. For example, "listen" and "silent" are
anagrams of each other.
"""


def is_anagram(s: str, t: str) -> bool:
    s = s.replace(" ", "").lower()
    t = t.replace(" ", "").lower()

    return sorted(s) == sorted(t)


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("Dormitory", "Dirty Room"))  # True
