# @lc app=leetcode id=2156 lang=python3
#
# [2156] Find Substring With Given Hash Value
#
# https://leetcode.com/problems/find-substring-with-given-hash-value/description/
#
# algorithms
# Hard (21.94%)
# Likes:    358
# Dislikes: 358
# Total Accepted:    10.7K
# Total Submissions: 48.6K
# Testcase Example:  '"leetcode"\n7\n20\n2\n0'
#
# The hash of a 0-indexed string s of length k, given integers p and m, is
# computed using the following function:
#
#
# hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) *
# p^k-1) mod m.
#
#
# Where val(s[i]) represents the index of s[i] in the alphabet from val('a') =
# 1 to val('z') = 26.
#
# You are given a string s and the integers power, modulo, k, and hashValue.
# Return sub, the first substring of s of length k such that hash(sub, power,
# modulo) == hashValue.
#
# The test cases will be generated such that an answer always exists.
#
# A substring is a contiguous non-empty sequence of characters within a
# string.
#
#
# Example 1:
#
#
# Input: s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
# Output: "ee"
# Explanation: The hash of "ee" can be computed to be hash("ee", 7, 20) = (5 *
# 1 + 5 * 7) mod 20 = 40 mod 20 = 0.
# "ee" is the first substring of length 2 with hashValue 0. Hence, we return
# "ee".
#
#
# Example 2:
#
#
# Input: s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
# Output: "fbx"
# Explanation: The hash of "fbx" can be computed to be hash("fbx", 31, 100) =
# (6 * 1 + 2 * 31 + 24 * 31^2) mod 100 = 23132 mod 100 = 32.
# The hash of "bxz" can be computed to be hash("bxz", 31, 100) = (2 * 1 + 24 *
# 31 + 26 * 31^2) mod 100 = 25732 mod 100 = 32.
# "fbx" is the first substring of length 3 with hashValue 32. Hence, we return
# "fbx".
# Note that "bxz" also has a hash of 32 but it appears later than "fbx".
#
#
#
# Constraints:
#
#
# 1 <= k <= s.length <= 2 * 10^4
# 1 <= power, modulo <= 10^9
# 0 <= hashValue < modulo
# s consists of lowercase English letters only.
# The test cases are generated such that an answer always exists.
#
#
#


# @lc code=start
import math
from typing import Callable


from enum import Enum

appr = Enum("approaches", "brute_force rolling_hash")
APPR = appr.rolling_hash


class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        if APPR == appr.brute_force:
            return self.subStrHash_brute_force(s, power, modulo, k, hashValue)
        if APPR == appr.rolling_hash:
            return self.subStrHash_rolling_hash(s, power, modulo, k, hashValue)
        return ""  # Never Reached

    def subStrHash_rolling_hash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        """
        O(N)
        https://leetcode.com/problems/find-substring-with-given-hash-value/solutions/1730118/reversed-rabin-karp-vs-inverse-modulo/
        """

        # modular arithmetic reference:
        # https://www.hackerearth.com/practice/math/number-theory/basic-number-theory-1/tutorial/
        # https://brilliant.org/wiki/modular-arithmetic/
        n = len(s)
        rolling_hash = 0
        val: Callable[[str], int] = lambda char: ord(char) - ord("a") + 1
        res = 0

        power_k_mod = pow(power, k, modulo)

        # step 1: [ val(s[n-1]) * p0 ] mod m
        # step 2: [ val(s[n-2]) * p0 + val(s[n-1]) * p1 ] mod m
        for i in range(n - 1, -1, -1):
            """
            Question:
                example solution is rolling_hash = (rolling_hash * power + val(s[i])) % modulo
                https://leetcode.com/problems/find-substring-with-given-hash-value/discuss/1730118/Reversed-Rabin-Karp-vs.-Inverse-Modulo
                this is without the (% modulo) after val(s[i])
                need to understand why this is mathematically valid

                rolling_hash = (rolling_hash - (power_kmod * val(s[i + k])) % modulo) % modulo
            """
            # add the new char hash and shift the power one up
            rolling_hash = (rolling_hash * power + val(s[i])) % modulo
            if i + k < n:
                # remove the last char hash
                rolling_hash = (rolling_hash - (power_k_mod * val(s[i + k]))) % modulo
            if rolling_hash == hashValue:
                res = i
        return s[res : res + k]

    def subStrHash_brute_force(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        """
        Although technically O(n)
        hash calculation of p^k-1 is too large to be calculated efficiently
        https://leetcode.com/problems/find-substring-with-given-hash-value/discuss/1730153/O(n)-solution-why-didn't-it-get-accepted-isn't-it-O(n)
        """

        for i in range(len(s) - (k - 1)):
            sub_str = s[i : i + k]
            if self.hash_str(sub_str, power, modulo) == hashValue:
                return sub_str
        return ""  # Never Reached

    def hash_str(self, s: str, power: int, modulo: int) -> int:
        """Calculate the hash for the given input

        ONLY used for naive verification or brute force approach
        """
        val: Callable[[str], int] = lambda char: ord(char) - ord("a") + 1
        return sum((val(s[i]) * pow(power, i, modulo) for i in range(len(s)))) % modulo

    # @lc code=end


def main():
    sol = Solution()
    s = "leetcode"
    power = 7
    modulo = 20
    k = 2
    hashValue = 0
    ans = sol.subStrHash(s, power, modulo, k, hashValue)
    print(ans)

    # s = "fbxzaad"
    # power = 31
    # modulo = 100
    # k = 3
    # hashValue = 32
    # ans = sol.subStrHash(s, power, modulo, k, hashValue)
    # print(ans)

    # s = "xxterzixjqrghqyeketqeynekvqhc"
    # power = 15
    # modulo = 94
    # k = 4
    # hashValue = 16
    # ans = sol.subStrHash(s, power, modulo, k, hashValue)
    # print(ans)


if __name__ == "__main__":
    main()
