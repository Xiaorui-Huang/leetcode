#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.com/problems/word-search/description/
#
# algorithms
# Medium (39.07%)
# Likes:    7902
# Dislikes: 302
# Total Accepted:    840.7K
# Total Submissions: 2.1M
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
#
#
# Example 1:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
#
#
# Example 2:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
#
#
# Example 3:
#
#
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
#
#
#
# Constraints:
#
#
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
#
#
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
#
#
from typing import Dict, List

# @lc code=start
from enum import Enum

approaches = Enum(
    "approaches", "BACKTRACK_SET BACKTRACK_HASH BACKTRACK_LC PRUNING BACKTRACK_TRIE"
)
APPROACH = approaches.BACKTRACK_TRIE


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if APPROACH == approaches.BACKTRACK_LC:
            return self.exist_BT_LC(board, word)
        elif APPROACH == approaches.BACKTRACK_SET:
            return self.exist_BT_SET(board, word)
        elif APPROACH == approaches.BACKTRACK_HASH:
            return self.exist_BT_HASH(board, word)
        elif APPROACH == approaches.PRUNING:
            return self.exist_STACK_PRUNING(board, word)
        elif APPROACH == approaches.BACKTRACK_TRIE:
            return self.exist_BT_TRIE(board, word)

    def exist_BT_TRIE(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols:
            return False

        trie = {}
        cur = trie
        for c in word:
            cur = cur.setdefault(c, {})
        # mark the end of the word
        cur["-"] = True

        def backtrack(i: int, j: int, trie: Dict) -> bool:
            if board[i][j] not in trie:
                return False

            letter = board[i][j]
            if "-" in trie[letter]:
                return True

            board[i][j] = "#"  # mark as exploring

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset
                if (
                    row < 0  # ensure that the search is within bounds
                    or rows <= row
                    or col < 0
                    or cols <= col
                ):
                    continue
                # although not an issue here in an actual trie there may be multiple letters we can keep on searching for
                # TODO:this can be optimized to not use a for loop... I'm just too lazy... refer to word search ii instead
                for subtrie in trie.values():
                    if backtrack(row, col, subtrie):
                        return True
            board[i][j] = letter  # revert back to avaliable for exploration
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, trie):
                    return True
        return False

    def exist_BT_HASH(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols:
            return False

        def backtrack(i: int, j: int, index: int) -> bool:
            if board[i][j] != word[index]:
                return False
            # if we dfs to the last index of the word and the last letter equals
            if ~index == -len(word):  # (redundant check) and board[i][j] == word[-1]:
                return True

            board[i][j] = "#"  # mark as exploring

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset
                if (
                    row < 0  # ensure that the search is within bounds
                    or rows <= row
                    or col < 0
                    or cols <= col
                ):
                    continue
                if backtrack(row, col, index + 1):
                    return True
            board[i][j] = word[index]  # revert back to avaliable for exploration
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, 0):
                    return True
        return False

    def exist_BT_SET(self, board: List[List[str]], word: str) -> bool:

        """Return if we can find the word in a sequential manner within the board (each letter is only allow to be used once)

        Idea:
            backtracking, we keep a set of visited cell, and for each cell we
            explore furthur using DFS algorithm in the 3 possible directions. if
            along any stack the word at index doesn't match the cell, then
            return false, revert the visited (so that the cell can be visited
            again) and keep searching. If all we reach the last char of the word
            and the word matches, we reach the base case each stack is resolves
            with a True return => True return for the algorithm

        Complexity:
            O[(MN) * 3^L] where M x N is the board size, and L is the length of
            the string At each cell of the board, we search for the word of L
            character and at each point there are practically 3 possible choices
            to search.

        Args:
            board (List[List[str]]): the board of letters
            word (str): the word we can to find in the board

        Returns:
            bool: if the word can be found within the board
        """
        rows = len(board)
        cols = len(board[0])
        if len(word) > rows * cols:
            return False
        visited = set()

        def backtrack(i: int, j: int, visited: set, index: int) -> bool:
            visited.add((i, j))
            if board[i][j] != word[index]:
                return False
            # if we dfs to the last index of the word and the last letter equals
            if ~index == -len(word):  # (redundant check) and board[i][j] == word[-1]:
                return True

            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                row, col = i + row_offset, j + col_offset
                if (
                    row < 0  # ensure that the search is within bounds
                    or rows <= row
                    or col < 0
                    or cols <= col
                    or (row, col)
                    in visited  # ensure that each letter is only visited once
                ):
                    continue
                if backtrack(row, col, visited, index + 1):
                    return True
                # otherwise backtrack on the path visited
                visited.remove((row, col))
            return False

        for i in range(rows):
            for j in range(cols):
                if backtrack(i, j, visited, 0):
                    return True
                # otherwise backtrack on the starting cell visited
                visited.remove((i, j))
        return False

    def exist_STACK_PRUNING(self, board, word):
        rows = len(board)
        cols = len(board[0])
        stack = []
        board_counter = {}

        # O(mn)
        for i in range(rows):
            for j in range(cols):
                char = board[i][j]
                if char == word[0]:
                    stack.append([i, j, 0])
                board_counter[char] = board_counter.get(char, 0) + 1

        # O(L)
        word_counter = {}
        for char in word:
            if char not in board_counter:
                return False
            word_counter[char] = word_counter.get(char, 0) + 1

        for char in word:
            # more occurrence of char in the word than in the board then False
            if board_counter[char] < word_counter[char]:
                return False

        # Confused AF
        visited = []
        while stack:
            i, j, index = stack.pop()

            if index <= len(visited):
                visited = visited[:index]

            # inefficiency? no?
            if [i, j] in visited:
                continue

            if index == len(word) - 1:
                if len(visited) == index:
                    return True
                continue

            visited.append([i, j])
            if i < rows - 1 and board[i + 1][j] == word[index + 1]:
                stack.append([i + 1, j, index + 1])
            if i > 0 and board[i - 1][j] == word[index + 1]:
                stack.append([i - 1, j, index + 1])
            if j < cols - 1 and board[i][j + 1] == word[index + 1]:
                stack.append([i, j + 1, index + 1])
            if j > 0 and board[i][j - 1] == word[index + 1]:
                stack.append([i, j - 1, index + 1])
        return False

    def exist_BT_LC(self, board: List[List[str]], word: str) -> bool:
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def backtrack(row, col, suffix):
            # Backtracking by altering the board along a search path, then reverting it back

            # bottom case: we find match for each letter in the word
            if len(suffix) == 0:
                return True

            # Check the current status, before jumping into backtracking
            if (
                row < 0
                or row == rows
                or col < 0
                or col == cols
                or board[row][col] != suffix[0]
            ):
                return False

            ret = False
            # mark the explored choice before exploring further.
            board[row][col] = "#"
            # explore the 4 neighbor directions
            for row_offset, col_offset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ret = backtrack(row + row_offset, col + col_offset, suffix[1:])
                # break instead of return directly to do some cleanup afterwards
                if ret:
                    break

            # revert the change, a clean slate and no side-effect
            board[row][col] = suffix[0]

            # Tried all directions, and did not find any match
            return ret

        for row in range(rows):
            for col in range(cols):
                if backtrack(row, col, word):
                    return True

        # no match found after all exploration
        return False


# @lc code=end


def main():
    sol = Solution()
    ans = sol.exist(
        # [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABZ"
        # [["a", "b"]], "ba",
        [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]],
        "ABCCED",
    )
    print(ans)


if __name__ == "__main__":
    main()
