# https://leetcode.com/problems/valid-anagram/description/

from collections import Counter

# Time O(N) | Mem O(1)
def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    return Counter(s) == Counter(t)

print(is_anagram("anagram", "nagaram")) # True
print(is_anagram("rat", "car")) # False
