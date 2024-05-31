# https://leetcode.com/problems/group-anagrams/description/

from typing import Iterable
from collections import defaultdict

def group_anagrams(strs: Iterable[str]) -> Iterable[Iterable[str]]:
    result = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        result[sorted_word].append(word)

    return result.values()
