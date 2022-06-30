#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.com/problems/happy-number/description/
#
# algorithms
# Easy (53.26%)
# Likes:    5800
# Dislikes: 742
# Total Accepted:    853.7K
# Total Submissions: 1.6M
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
#
#
# Return true if n is a happy number, and false if not.
#
#
# Example 1:
#
#
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
#
#
# Example 2:
#
#
# Input: n = 2
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur_sum = self.digit_square_sum(n)

        while cur_sum != 1:
            cur_sum = self.digit_square_sum(cur_sum)
            if cur_sum in seen:
                # case 2: loops
                return False
            seen.add(cur_sum)

        # case 1: equals 1
        return True
        # case 3: increase to infinity, cannot happen e.g. digit_square_sum(999) -> 243

    def digit_square_sum(self, n: int) -> int:
        sum = 0
        while n:
            sum += (n % 10) ** 2
            n //= 10
        return sum


# @lc code=end

def main():
    sol = Solution()
    ans = sol.isHappy(19)
    print(ans)


if __name__ == "__main__":
    main()
