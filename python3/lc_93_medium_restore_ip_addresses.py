#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (43.93%)
# Likes:    3929
# Dislikes: 704
# Total Accepted:    358.8K
# Total Submissions: 791.8K
# Testcase Example:  '"25525511135"'
#
# A valid IP address consists of exactly four integers separated by single
# dots. Each integer is between 0 and 255 (inclusive) and cannot have leading
# zeros.
#
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but
# "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP
# addresses.
#
#
# Given a string s containing only digits, return all possible valid IP
# addresses that can be formed by inserting dots into s. You are not allowed to
# reorder or remove any digits in s. You may return the valid IP addresses in
# any order.
#
#
# Example 1:
#
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]
#
#
# Example 2:
#
#
# Input: s = "0000"
# Output: ["0.0.0.0"]
#
#
# Example 3:
#
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 20
# s consists of digits only.
#

# @lc code=start
"""
take or not take the current digit for this ip position
"""


class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        n = len(s)
        ip: list[str] = []
        valid_ips = []

        def backtrack(index: int, integer_count: int) -> None:
            # we have iterated through every digit
            if index == n:
                # only add ip that has used all digits and have 4 integers
                if integer_count == 4:
                    valid_ips.append("".join(ip))
                return

            # we have tried more than 4 integers, we can early abort
            if integer_count > 4:
                return

            # starting a new ip pos
            if not ip or ip[-1] == ".":
                ip.append(s[index])
                backtrack(index + 1, integer_count)
                ip.pop()
                return

            # ensure we only add this ip if
            # 1. it's between 0 and 255
            # 2. it doesn't start with 0
            # 3. we can either add another number and see if it's valid or let the cur_ip be the entire ip at this position

            ip.append(".")
            # trying a new integer => ip_pos + 1
            backtrack(index, integer_count + 1)
            ip.pop()

            cur_ip = int(ip[-1])
            if cur_ip == 0:  # adding anything will result in a leading 0, abort
                return

            cur_ip = cur_ip * 10 + int(s[index])
            if cur_ip > 255:  # abort if it's an invalid number
                return

            ip[-1] = str(cur_ip)
            backtrack(index + 1, integer_count)

        backtrack(0, 1)
        return valid_ips


# @lc code=end


def main() -> None:
    sol = Solution()
    s = "0000"
    ans = sol.restoreIpAddresses(s)
    print(ans)

    s = "25525511135"
    ans = sol.restoreIpAddresses(s)
    print(ans)

    s = "101023"
    ans = sol.restoreIpAddresses(s)
    print(ans)


if __name__ == "__main__":
    main()
