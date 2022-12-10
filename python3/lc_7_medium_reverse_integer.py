#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (27.19%)
# Likes:    9108
# Dislikes: 11167
# Total Accepted:    2.4M
# Total Submissions: 8.7M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
#
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    # A 32-bit signed integer. It has a minimum value of -2,147,483,648 and a
    # maximum value of 2,147,483,647 (inclusive).

    def reverse(self, x: int) -> int:
        limit = 2**31 - 1
        prior_digits = limit // 10
        last_digit = limit % 10

        counter = 0
        signed = False
        trailing_zeros = True
        if x < 0:
            x *= -1
            signed = True

        num = 0
        while x:
            digit = x % 10

            if digit:
                trailing_zeros = False
            if not trailing_zeros:
                counter += 1
            if counter == 10:
                if num > prior_digits or (num == prior_digits and digit > last_digit + int(signed)):
                    return 0

            x //= 10
            num = num * 10 + digit

        return -num if signed else num


# @lc code=end
def main() -> None:
    sol = Solution()
    num = -7463847412
    assert -(2**31) <= num <= 2**31 - 1
    ans = sol.reverse(num)
    print(ans)


if __name__ == "__main__":
    main()
