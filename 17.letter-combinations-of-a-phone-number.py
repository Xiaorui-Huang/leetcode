#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (54.05%)
# Likes:    10303
# Dislikes: 684
# Total Accepted:    1.2M
# Total Submissions: 2.2M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
#
# A mapping of digit to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
#
#
#
#
# Example 1:
#
#
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#
#
# Example 2:
#
#
# Input: digits = ""
# Output: []
#
#
# Example 3:
#
#
# Input: digits = "2"
# Output: ["a","b","c"]
#
#
#
# Constraints:
#
#
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
#
#
#

# @lc code=start
class Solution:
    mem = {
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
    }

    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        if digits in self.mem:
            return self.mem[digits]

        for i in range(0, len(digits) - 1):
            comb = []
            cur_digit = digits[i]
            sub_digits = digits[i + 1 :]

            sub_comb = self.letterCombinations(sub_digits)
            for letter in self.mem[cur_digit]:
                for string_comb in sub_comb:
                    comb.append(letter + string_comb)
            self.mem[cur_digit + sub_digits] = comb

        return self.mem[digits]


# @lc code=end


def main():
    sol = Solution()
    digits = "3"
    ans = sol.letterCombinations(digits)
    print(ans)


if __name__ == "__main__":
    main()
