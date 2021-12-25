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
from typing import Dict, List

# @lc code=start


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
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
        found = set()  # just to manage possible duplicate words in the broad

        def backtrack(i: int, j: int, trie: Dict, prefix: str) -> None:
            if None in trie:
                found.add(prefix + board[i][j])
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

                # brach to each possible letter
                for c in trie:
                    # only continue searching valid letters in trie according to
                    # the next cell we are searching for 

                    # Note: Cannot use if c is not None: -> we maybe going down
                    # a hole thar uses a None ending for a word, but actually
                    # searching a cell with a different letter, i.e. using word
                    # hf's None ending, but seaching cell k. so we end up with
                    # word hf
                    if c == board[row][col]:
                        backtrack(row, col, trie[c], prefix + letter)

            board[i][j] = letter

        # run search on each cell
        for i in range(rows):
            for j in range(cols):
                letter = board[i][j]
                if letter in trie:
                    backtrack(i, j, trie[letter], "")

        return found


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
