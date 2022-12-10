#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Medium (45.57%)
# Likes:    10035
# Dislikes: 227
# Total Accepted:    935.6K
# Total Submissions: 2M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the
# police.
#
#
# Example 1:
#
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
#
# Example 2:
#
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
#
#
# Constraints:
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400
#
#
#

# @lc code=start
class Solution:
    def rob(self, nums: list[int]) -> int:
        """Return the maximum amount we can rob without triggering the alarm

        Idea:
            define OPT(i) = the max amount we can rob given nums[:i]; n = len(nums)

            OPT(i) = max(OPT(n-1), OPT(n-2) + nums[i])
            That is the max of wither not robbing the current house (and enjoy the fruits from house i-1)
            or robbing the current house (and enjoy the fruits from house i-2)

            Base case:  n = 1 -> return nums[0]
                        n = 2 -> return max(nums)
            Final Results: OPT(n)

        Args:
            nums (list[int]): Money stashes in houses

        Returns:
            int: Max amount we can possibly rob
        """
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)

        # equivalent to OPT(i-2) and OPT(i-1)
        two_house_before, one_house_before = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            # to rob or not to rob, that is the question
            money_on_hand = max(one_house_before, two_house_before + nums[i])
            two_house_before = one_house_before
            one_house_before = money_on_hand

        return money_on_hand


# @lc code=end
def main() -> None:
    sol = Solution()
    ans = sol.rob([2, 1, 1, 2])
    print(ans)


if __name__ == "__main__":
    main()
