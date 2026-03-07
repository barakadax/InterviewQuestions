# https://leetcode.com/problems/group-anagrams/description/

from typing import Iterable
from collections import defaultdict

# Time O(N * M) | Mem O(N * M)
def group_anagrams(strs: Iterable[str]) -> Iterable[Iterable[str]]:
    result: defaultdict = defaultdict(list)

    for word in strs:
        counter: list[int] = [0] * 26
        for char in word:
            counter[ord(char) - ord('a')] += 1

        result[tuple(counter)].append(word)

    return result.values()


print(group_anagrams(["eat","tea","tan","ate","nat","bat"])) # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
