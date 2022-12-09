#
# @lc app=leetcode id=2491 lang=python3
#
# [2491] Divide Players Into Teams of Equal Skill
#
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/
#
# algorithms
# Medium (58.02%)
# Likes:    189
# Dislikes: 1
# Total Accepted:    16.7K
# Total Submissions: 28.9K
# Testcase Example:  '[3,2,5,1,3,4]'
#
# You are given a positive integer array skill of even length n where skill[i]
# denotes the skill of the i^th player. Divide the players into n / 2 teams of
# size 2 such that the total skill of each team is equal.
#
# The chemistry of a team is equal to the product of the skills of the players
# on that team.
#
# Return the sum of the chemistry of all the teams, or return -1 if there is no
# way to divide the players into teams such that the total skill of each team
# is equal.
#
#
# Example 1:
#
#
# Input: skill = [3,2,5,1,3,4]
# Output: 22
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where
# each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 +
# 9 = 22.
#
#
# Example 2:
#
#
# Input: skill = [3,4]
# Output: 12
# Explanation:
# The two players form a team with a total skill of 7.
# The chemistry of the team is 3 * 4 = 12.
#
#
# Example 3:
#
#
# Input: skill = [1,1,2,3]
# Output: -1
# Explanation:
# There is no way to divide the players into teams such that the total skill of
# each team is equal.
#
#
#
# Constraints:
#
#
# 2 <= skill.length <= 10^5
# skill.length is even.
# 1 <= skill[i] <= 1000
#
#
#

# @lc code=start
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        """Question 1 two sum but on steroids"""
        skill_dict: dict[int, int] = {}
        skill_sum = 0
        # calculate the skill sum to know the skills per team, while building a player dictionary
        for skill_level in skill:
            skill_sum += skill_level
            skill_dict[skill_level] = skill_dict.get(skill_level, 0) + 1

        n_teams = len(skill) // 2
        if skill_sum % n_teams != 0:
            return -1

        target = skill_sum // n_teams

        chemistry = 0
        for _ in range(n_teams):
            # remove a player and try find a match
            skill_level, number_of = skill_dict.popitem()
            # insert the other players with the same skill level if there exists
            if number_of > 1:
                skill_dict[skill_level] = number_of - 1

            complement_skill_level = target - skill_level
            if complement_skill_level not in skill_dict:
                return -1

            number_of = skill_dict.pop(complement_skill_level)
            if number_of > 1:
                skill_dict[complement_skill_level] = number_of - 1

            chemistry += skill_level * complement_skill_level

        return chemistry


# @lc code=end
