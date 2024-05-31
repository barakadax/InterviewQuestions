# https://leetcode.com/problems/valid-anagram/description/

def is_anagram(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
