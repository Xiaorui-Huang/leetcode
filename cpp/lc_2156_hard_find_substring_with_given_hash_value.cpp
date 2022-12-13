/*
 * @lc app=leetcode id=2156 lang=cpp
 *
 * [2156] Find Substring With Given Hash Value
 *
 * https://leetcode.com/problems/find-substring-with-given-hash-value/description/
 *
 * algorithms
 * Hard (21.94%)
 * Likes:    358
 * Dislikes: 358
 * Total Accepted:    10.7K
 * Total Submissions: 48.6K
 * Testcase Example:  '"leetcode"\n7\n20\n2\n0'
 *
 * The hash of a 0-indexed string s of length k, given integers p and m, is
 * computed using the following function:
 *
 *
 * hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) *
 * p^k-1) mod m.
 *
 *
 * Where val(s[i]) represents the index of s[i] in the alphabet from val('a') =
 * 1 to val('z') = 26.
 *
 * You are given a string s and the integers power, modulo, k, and hashValue.
 * Return sub, the first substring of s of length k such that hash(sub, power,
 * modulo) == hashValue.
 *
 * The test cases will be generated such that an answer always exists.
 *
 * A substring is a contiguous non-empty sequence of characters within a
 * string.
 *
 *
 * Example 1:
 *
 *
 * Input: s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
 * Output: "ee"
 * Explanation: The hash of "ee" can be computed to be hash("ee", 7, 20) = (5 *
 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0.
 * "ee" is the first substring of length 2 with hashValue 0. Hence, we return
 * "ee".
 *
 *
 * Example 2:
 *
 *
 * Input: s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
 * Output: "fbx"
 * Explanation: The hash of "fbx" can be computed to be hash("fbx", 31, 100) =
 * (6 * 1 + 2 * 31 + 24 * 31^2) mod 100 = 23132 mod 100 = 32.
 * The hash of "bxz" can be computed to be hash("bxz", 31, 100) = (2 * 1 + 24 *
 * 31 + 26 * 31^2) mod 100 = 25732 mod 100 = 32.
 * "fbx" is the first substring of length 3 with hashValue 32. Hence, we return
 * "fbx".
 * Note that "bxz" also has a hash of 32 but it appears later than "fbx".
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= k <= s.length <= 2 * 10^4
 * 1 <= power, modulo <= 10^9
 * 0 <= hashValue < modulo
 * s consists of lowercase English letters only.
 * The test cases are generated such that an answer always exists.
 *
 *
 */
#include <algorithm>
#include <cmath>
#include <iostream>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}

// @lc code=start
class Solution {
  public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        uint64_t power_k_mod = modpow(power, k, modulo);
        uint64_t rolling_hash = 0;
        int n = s.length();
        int res = 0;

        auto val = [](char ch) -> int { return int(ch) - int('a') + 1; };
        for (int i = n - 1; i >= 0; i--) {
            rolling_hash = (rolling_hash * power + val(s[i])) % modulo;

            if (i + k < n)
                // plus modulo to ensure the mod is positive
                // modulo of negative numbers https://stackoverflow.com/a/44197900
                rolling_hash = (modulo + rolling_hash - power_k_mod * val(s[i + k]) % modulo) % modulo;
            if (rolling_hash == hashValue)
                res = i;
        }
        return s.substr(res, k);
    };

  private:
    // Reference to avoiding overflow
    // https://stackoverflow.com/questions/52063315/modular-exponentiation-overflows-when-using-multiple-of-two-uint-32-numbers
    uint64_t modpow(int base, int exp, int mod) {
        uint64_t product = 1;
        base = base % mod;
        while (exp > 0) {
            if (exp & 1)
                product = modmult(product, base, mod);
            base = modmult(base, base, mod);
            exp >>= 1;
        }
        return product;
    }
    uint64_t modmult(uint64_t a, uint64_t b, uint64_t mod) {
        if (a == 0 || b < mod / a)
            return (a * b) % mod;
        uint64_t sum = 0;
        while (b > 0) {
            if (b & 1)
                sum = modadd(sum, a, mod);
            a = modadd(a, a, mod);
            b >>= 1;
        }
        return sum;
    }
    uint64_t modadd(uint64_t a, uint64_t b, uint64_t mod) {
        // Ensure Precondition: a < mod, b < mod
        if (a >= mod)
            a %= mod;
        if (b >= mod)
            b %= mod;

        a += b;
        if (a >= mod || a < b)
            a -= mod;
        return a;
    }
};
// @lc code=end