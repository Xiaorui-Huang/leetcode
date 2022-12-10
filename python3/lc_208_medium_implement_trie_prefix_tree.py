#
# @lc app=leetcode id=208 lang=python3
#
# [208] Implement Trie (Prefix Tree)
#
# https://leetcode.com/problems/implement-trie-prefix-tree/description/
#
# algorithms
# Medium (56.18%)
# Likes:    6051
# Dislikes: 83
# Total Accepted:    511.2K
# Total Submissions: 907.3K
# Testcase Example:  '["Trie","insert","search","search","startsWith","insert","search"]\n' +
# '[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]'
#
# A trie (pronounced as "try") or prefix tree is a tree data structure used to
# efficiently store and retrieve keys in a dataset of strings. There are
# various applications of this data structure, such as autocomplete and
# spellchecker.
#
# Implement the Trie class:
#
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie
# (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously
# inserted string word that has the prefix prefix, and false otherwise.
#
#
#
# Example 1:
#
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
#
# Constraints:
#
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 10^4 calls in total will be made to insert, search, and
# startsWith.
#
#
#

# @lc code=start
from enum import Enum
from typing import Any

approaches = Enum("approaches", "NAIVE FAST")
APPROACH = approaches.FAST


class Trie:
    if APPROACH == approaches.FAST:

        def __init__(self) -> None:
            self.trie: dict[str, Any] = {}

        def insert(self, word: str) -> None:
            trie = self.trie
            for c in word:
                # if c not in trie:
                #     trie[c] = {}
                # trie = trie[c]

                # Using more consice code
                trie = trie.setdefault(c, {})

            trie["-"] = True

        def search(self, word: str) -> bool:
            trie = self.trie
            for c in word:
                if c not in trie:
                    return False
                trie = trie[c]
            return "-" in trie

        def startsWith(self, prefix: str) -> bool:
            trie = self.trie
            for c in prefix:
                if c not in trie:
                    return False
                trie = trie[c]
            return True

    elif APPROACH == approaches.NAIVE:

        def __init__(self) -> None:
            self.tries: dict[str, tuple[Trie, bool]] = {}

        def insert(self, word: str) -> None:
            if not word:
                return

            c, rem = word[0], word[1:]
            end = False
            if c not in self.tries:
                # create a new trie
                trie = Trie()
            else:
                trie, end = self.tries[c]

            if rem:
                # make previous ending mark persistence with insert
                self.tries[c] = (trie, False or end)
            else:
                # 1 indicating that this is a end of a word
                self.tries[c] = (trie, True)
            trie.insert(rem)

        def search(self, word: str) -> bool:
            if not word:
                return True

            c, rem = word[0], word[1:]
            if c not in self.tries:
                return False

            trie, end = self.tries[c]
            if rem:
                return trie.search(rem)
            else:
                return end and trie.search(rem)

        def startsWith(self, prefix: str) -> bool:
            if not prefix:
                return True

            c, rem = prefix[0], prefix[1:]
            if c not in self.tries:
                return False

            return self.tries[c][0].startsWith(rem)


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end


def main() -> None:
    trie = Trie()

    trie.insert("app")
    trie.insert("apple")

    ans = trie.search("apps")  # return True
    print(ans)
    ans = trie.search("app")  # return False
    print(ans)


if __name__ == "__main__":
    main()
