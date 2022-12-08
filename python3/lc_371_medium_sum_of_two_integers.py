#
# @lc app=leetcode id=371 lang=python3
#
# [371] Sum of Two Integers
#
# https://leetcode.com/problems/sum-of-two-integers/description/
#
# algorithms
# Medium (50.66%)
# Likes:    2137
# Dislikes: 3275
# Total Accepted:    262.3K
# Total Submissions: 517.9K
# Testcase Example:  '1\n2'
#
# Given two integers a and b, return the sum of the two integers without using
# the operators + and -.
#
#
# Example 1:
# Input: a = 1, b = 2
# Output: 3
# Example 2:
# Input: a = 2, b = 3
# Output: 5
#
#
# Constraints:
#
#
# -1000 <= a, b <= 1000

# @lc code=start
class Solution:
    def getSum(self, a: int, b: int) -> int:
        x, y = abs(a), abs(b)

        # ensure we are doing x+y or x-y operations
        if x < y:
            return self.getSum(b, a)
        sign = -1 if a < 0 else 1

        # xor is add withoug accounting for carry
        # so we add the carry until there is no carry
        # and the carry is just x and y operation
        
        # xor is subtract withoug accounting for borrows
        # so we substract the borrow until there is no borrow
        # and the borrow is just (not x) and y operation
        
        # both a and b are negative or positive
        if a * b >= 0:
            while y != 0:
                carry = x & y
                x = x ^ y
                y = carry << 1
        else:
            while y != 0:
                borrow = (~x) & y
                x = x ^ y
                y = borrow << 1
        return sign * x

sol = Solution()
a = sol.getSum(-1,1)
print(a)
            



# @lc code=end
