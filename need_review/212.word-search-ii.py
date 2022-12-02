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
from enum import Enum

approaches = Enum("approaches", "LC OWN")
APPROACH = approaches.OWN


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        if APPROACH == approaches.LC:
            return self.findWords_LC(board, words)
        elif APPROACH == approaches.OWN:
            return self.findWords_OWN(board, words)
        return []  # never reached

    def findWords_OWN(self, board: list[list[str]], words: list[str]) -> list[str]:
        # constructing a trie
        trie: dict = {}
        for word in words:
            cur = trie
            for letter in word:
                cur = cur.setdefault(letter, {})
            cur[None] = None  # marks the end of a word

        del word, letter, cur  # clean ups from trie construction

        rows = len(board)
        cols = len(board[0])
        found = list()

        def backtrack(i: int, j: int, parent_trie: dict, prefix: str) -> None:
            letter = board[i][j]
            cur_trie = parent_trie[letter]
            word = prefix + letter
            if None in cur_trie:
                # end of word -> found the word. to prevent duplicates remove the end of word marker
                cur_trie.pop(None)
                # not a single word search so we don't return and keep searching
                found.append(word)

            board[i][j] = "#"

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset
                if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] not in cur_trie:
                    continue
                backtrack(row, col, cur_trie, word)

            board[i][j] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not cur_trie:
                parent_trie.pop(letter)

        # run search on each cell
        for i in range(rows):
            for j in range(cols):
                letter = board[i][j]
                if letter in trie:
                    backtrack(i, j, trie, "")

        return found

    def findWords_LC(self, board: list[list[str]], words: list[str]) -> list[str]:
        WORD_KEY = "$"

        # smart! implementing the word as the word ending marker
        trie: dict = {}
        for word in words:
            cur = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                cur = cur.setdefault(letter, {})
            # mark the existence of a word in trie node
            cur[WORD_KEY] = word  # NB

        del cur, word, letter

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
                matched.append(word_match)  # word is stored at WORD_KEY

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for (rowOffset, colOffset) in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if (
                    newRow < 0
                    or newRow >= rows
                    or newCol < 0
                    or newCol >= cols
                    or not board[newRow][newCol] in currNode
                ):
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
