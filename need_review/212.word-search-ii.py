#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (38.47%)
# Likes:    5186
# Dislikes: 179
# Total Accepted:    384.7K
# Total Submissions: 999.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n' +
#  '["oath","pea","eat","rain"]'
#
# Given an m x n board of characters and a list of strings words, return all
# words on the board.
#
# Each word must be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once in a word.
#
#
# Example 1:
#
#
# Input: board =
# [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
# words = ["oath","pea","eat","rain"]
# Output: ["eat","oath"]
#
#
# Example 2:
#
#
# Input: board = [["a","b"],["c","d"]], words = ["abcb"]
# Output: []
#
#
#
# Constraints:
#
#
# m == board.length
# n == board[i].length
# 1 <= m, n <= 12
# board[i][j] is a lowercase English letter.
# 1 <= words.length <= 3 * 10^4
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# All the strings of words are unique.
#
#
#


# @lc code=start
from typing import Dict, List
from enum import Enum

approaches = Enum("approaches", "LC OWN")
APPROACH = approaches.LC


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if APPROACH == approaches.LC:
            return self.findWords_LC(board, words)
        elif APPROACH == approaches.OWN:
            return self.findWords_OWN(board, words)

    def findWords_OWN(self, board: List[List[str]], words: List[str]) -> List[str]:
        # constructing a trie
        trie = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur[None] = None  # marks the end of a word

        del word, letter, cur  # clean ups

        rows = len(board)
        cols = len(board[0])
        found = list()

        def backtrack(i: int, j: int, trie: Dict, prefix: str) -> None:
            if None in trie:
                trie.pop(
                    None
                )  # found the word no need to add it again, if there is a duplicate
                found.append(prefix + board[i][j])
                # don't stop searching so we don't return

            letter = board[i][j]
            board[i][j] = "#"

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset
                if (
                    row < 0
                    or col < 0
                    or row >= rows
                    or col >= cols
                    or board[row][col] not in trie
                ):
                    continue
                backtrack(row, col, board[row][col], prefix + letter)

            board[i][j] = letter

        # run search on each cell
        for i in range(rows):
            for j in range(cols):
                letter = board[i][j]
                if letter in trie:
                    backtrack(i, j, trie[letter], "")

        return found

    def findWords_LC(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"

        # smart! implementing the word as the word ending marker
        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rows = len(board)
        cols = len(board[0])

        matched = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matched.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if newRow < 0 or newRow >= rows or newCol < 0 or newCol >= cols:
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rows):
            for col in range(cols):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matched


# @lc code=end
def main():
    sol = Solution()
    ans = sol.findWords(
        # [
        #     ["o", "a", "a", "n"],
        #     ["a", "t", "a", "e"],
        #     ["p", "h", "a", "r"],
        #     ["p", "l", "e", "n"],
        # ],
        # ["app", "apple", "oath", "pea", "eat", "rain"],
        # [
        #     ["o", "a", "b", "n"],
        #     ["o", "t", "a", "e"],
        #     ["a", "h", "k", "r"],
        #     ["a", "f", "l", "v"],
        # ],
        # ["oa", "oaa"],
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["oath", "pea", "eat", "rain", "hklf", "hf"],
    )
    print(ans)


if __name__ == "__main__":
    main()
