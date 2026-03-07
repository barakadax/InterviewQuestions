# https://leetcode.com/problems/word-ladder-ii/description/

from collections import defaultdict, deque

class Solution:
    # Time: O(N) | Space: O(N)
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        self.adj = defaultdict(list)
        self.distances = {beginWord: 0}
        self.results = []

        queue: deque = deque([beginWord])
        found: bool = False

        while queue and not found:
            visited_this_level: dict = {}
            for _ in range(len(queue)):
                curr_word = queue.popleft()

                for i in range(len(curr_word)):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = curr_word[:i] + char + curr_word[i+1:]

                        if next_word in wordSet:
                            if next_word not in self.distances or self.distances[next_word] == self.distances[curr_word] + 1:
                                self.adj[curr_word].append(next_word)

                                if next_word not in self.distances:
                                    visited_this_level[next_word] = self.distances[curr_word] + 1
                                    queue.append(next_word)
                                    if next_word == endWord:
                                        found = True

            self.distances.update(visited_this_level)

        if found:
            self._backtrack(beginWord, endWord, [beginWord])

        return self.results

    # Time: O(N) | Mem O(N) - Breadth-First Search
    def _backtrack(self, curr: str, target: str, path: list[str]):
        if curr == target:
            self.results.append(list(path))
            return

        if curr not in self.adj:
            return

        for neighbor in self.adj[curr]:
            if self.distances.get(neighbor) == self.distances[curr] + 1:
                path.append(neighbor)
                self._backtrack(neighbor, target, path)
                path.pop()

s: Solution = Solution()
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"])) # [['hit', 'hot', 'dot', 'dog', 'cog'], ['hit', 'hot', 'lot', 'log', 'cog']]
print(s.findLadders("hit", "cog", ["hot","dot","dog","lot","log"])) # []
