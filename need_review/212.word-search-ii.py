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
from typing import List

# @lc code=start


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # constructing a trie
        trie = {}
        for word in words:
            cur = trie
            for c in word:
                if c not in cur:
                    cur[c] = {}
                cur = cur[c]
            cur["-"] = True  # marks the end of a word

        A = board
        rows = len(A)
        cols = len(A[0])
        
        # def backtrack(i, j, )


# @lc code=end
def main():
    sol = Solution()
    ans = sol.findWords(
        [
            ["o", "a", "a", "n"],
            ["e", "t", "a", "e"],
            ["i", "h", "k", "r"],
            ["i", "f", "l", "v"],
        ],
        ["app", "apple", "oath", "pea", "eat", "rain"],
    )
    print(ans)


if __name__ == "__main__":
    main()
