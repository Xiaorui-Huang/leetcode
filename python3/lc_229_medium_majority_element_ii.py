#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (42.24%)
# Likes:    4691
# Dislikes: 278
# Total Accepted:    282.3K
# Total Submissions: 668.2K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
#
#
# Example 1:
#
#
# Input: nums = [3,2,3]
# Output: [3]
#
#
# Example 2:
#
#
# Input: nums = [1]
# Output: [1]
#
#
# Example 3:
#
#
# Input: nums = [1,2]
# Output: [1,2]
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 5 * 10^4
# -10^9 <= nums[i] <= 10^9
#
#
#
# Follow up: Could you solve the problem in linear time and in O(1) space?
#
#


# Boyer-Moore majority vote algorithm
# https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
# https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration

# @lc code=start


class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        """Return all the elements that appears more than ⌊ n/3 ⌋ times.
        Uses Boyer-Moore algorithm, essentially keep track of the relative count
        instead of the absolute count

        Args:
            nums (list[int]): list of elements

        Returns:
            list[int]: list of majority elements
        """
        # since we only want elements that appears more than ⌊ n/3 ⌋ times.
        # there is only a maximum of two potential candidates

        if not nums:
            return []

        count1, count2, candidate1, candidate2 = 0, 0, None, None

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [candidate for candidate in (candidate1, candidate2) if nums.count(candidate) > len(nums) // 3]  # type: ignore


# @lc code=end
def main() -> None:
    sol = Solution()
    lst = [1, 2]
    ans = sol.majorityElement(lst)
    print(ans)


if __name__ == "__main__":
    main()
