#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#
# https://leetcode.com/problems/gas-station/description/
#
# algorithms
# Medium (45.14%)
# Likes:    8871
# Dislikes: 759
# Total Accepted:    531.6K
# Total Submissions: 1.2M
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# There are n gas stations along a circular route, where the amount of gas at
# the i^th station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to
# travel from the i^th station to its next (i + 1)^th station. You begin the
# journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's
# index if you can travel around the circuit once in the clockwise direction,
# otherwise return -1. If there exists a solution, it is guaranteed to be
# unique
#
#
# Example 1:
#
#
# Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# Output: 3
# Explanation:
# Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 +
# 4 = 4
# Travel to station 4. Your tank = 4 - 1 + 5 = 8
# Travel to station 0. Your tank = 8 - 2 + 1 = 7
# Travel to station 1. Your tank = 7 - 3 + 2 = 6
# Travel to station 2. Your tank = 6 - 4 + 3 = 5
# Travel to station 3. The cost is 5. Your gas is just enough to travel back to
# station 3.
# Therefore, return 3 as the starting index.
#
#
# Example 2:
#
#
# Input: gas = [2,3,4], cost = [3,4,3]
# Output: -1
# Explanation:
# You can't start at station 0 or 1, as there is not enough gas to travel to
# the next station.
# Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 =
# 4
# Travel to station 0. Your tank = 4 - 3 + 2 = 3
# Travel to station 1. Your tank = 3 - 3 + 3 = 3
# You cannot travel back to station 2, as it requires 4 unit of gas but you
# only have 3.
# Therefore, you can't travel around the circuit once no matter where you
# start.
#
#
#
# Constraints:
#
#
# n == gas.length == cost.length
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#

# @lc code=start
from enum import Enum

appr = Enum("approaches", "one_pass prefix_sum")
APPR = appr.one_pass


class Solution:
    def canCompleteCircuit(self, gases: list[int], costs: list[int]) -> int:
        match APPR:
            case appr.one_pass:
                return self.canCompleteCircuit_one_pass(gases, costs)
            case appr.prefix_sum:
                return self.canCompleteCircuit_one_pass(gases, costs)
            case _:
                return 0  # type: ignore

    def canCompleteCircuit_one_pass(self, gases: list[int], costs: list[int]) -> int:
        total_surplus, surplus, start = 0, 0, 0
        for i, (gas, cost) in enumerate(zip(gases, costs)):
            total_surplus += gas - cost
            surplus += gas - cost
            if surplus < 0:
                surplus = 0
                start = i + 1

        return start if total_surplus >= 0 else -1

    def canCompleteCircuit_prefix_sum(self, gases: list[int], costs: list[int]) -> int:
        n = len(gases)
        diff = [gas - cost for gas, cost in zip(gases, costs)]
        deficit = diff[0]  # record the most ACCUMULATIVELY gas intensive stage of the whole trip (min of prefix_sum)

        running_sum = 0
        for profit in diff:
            running_sum += profit
            deficit = min(deficit, running_sum)

        target = running_sum  # the amount of gas that should be remaining after a full trip
        if target < 0:  # prefix-sum has a net negative, impossible to circulate
            return -1

        running_sum = 0
        for i_rev, profit in enumerate(reversed(diff)):
            running_sum += profit
            if running_sum + deficit == target:
                return n - 1 - i_rev  # convert a reversed index to a forward index

        return 0  # Never Reached, since there is a guaranteed answer


# @lc code=end
