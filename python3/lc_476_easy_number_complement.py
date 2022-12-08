#
# @lc app=leetcode id=476 lang=python3
#
# [476] Number Complement
#
# https://leetcode.com/problems/number-complement/description/
#
# algorithms
# Easy (65.51%)
# Likes:    1409
# Dislikes: 92
# Total Accepted:    226.4K
# Total Submissions: 345.3K
# Testcase Example:  '5'
#
# The complement of an integer is the integer you get when you flip all the 0's
# to 1's and all the 1's to 0's in its binary representation.
#
#
# For example, The integer 5 is "101" in binary and its complement is "010"
# which is the integer 2.
#
#
# Given an integer num, return its complement.
#
#
# Example 1:
#
#
# Input: num = 5
# Output: 2
# Explanation: The binary representation of 5 is 101 (no leading zero bits),
# and its complement is 010. So you need to output 2.
#
#
# Example 2:
#
#
# Input: num = 1
# Output: 0
# Explanation: The binary representation of 1 is 1 (no leading zero bits), and
# its complement is 0. So you need to output 0.
#
#
#
# Constraints:
#
#
# 1 <= num < 2^31
#
#
#
# Note: This question is the same as 1009:
# https://leetcode.com/problems/complement-of-base-10-integer/
#
#

# @lc code=start
from enum import Enum

approaches = Enum("approaches", "BITMASK_CALC BITMASK_HIGHEST_PROPAGATE")
APPROACH = approaches.BITMASK_HIGHEST_PROPAGATE


class Solution:
    if APPROACH == approaches.BITMASK_CALC:

        def findComplement(self, num: int) -> int:
            # uses xor to flip the bits against all 1's
            # 2^bits - 1 is all ones
            return num ^ (2 ** (num.bit_length()) - 1)

    elif APPROACH == approaches.BITMASK_HIGHEST_PROPAGATE:

        def findComplement(self, num: int) -> int:
            # bitmask has the same length as num and contains only ones 1...1
            # This propagatest the highest bit down to the all less significant bits
            bitmask = num
            bitmask |= bitmask >> 1
            bitmask |= bitmask >> 2
            bitmask |= bitmask >> 4
            bitmask |= bitmask >> 8
            bitmask |= bitmask >> 16
            # flip all bits
            return bitmask ^ num


# @lc code=end


def main():
    sol = Solution()
    num = 4738
    ans = sol.findComplement(num)
    print(f"{num:b}\n{ans:{num.bit_length()}b}")
    print(f"{num}\n{ans}")


if __name__ == "__main__":
    main()
