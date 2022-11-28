/*
 * @lc app=leetcode id=42 lang=cpp
 *
 * [42] Trapping Rain Water
 *
 * https://leetcode.com/problems/trapping-rain-water/description/
 *
 * algorithms
 * Hard (58.74%)
 * Likes:    23915
 * Dislikes: 332
 * Total Accepted:    1.4M
 * Total Submissions: 2.4M
 * Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
 *
 * Given n non-negative integers representing an elevation map where the width
 * of each bar is 1, compute how much water it can trap after raining.
 *
 *
 * Example 1:
 *
 *
 * Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
 * Output: 6
 * Explanation: The above elevation map (black section) is represented by array
 * [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue
 * section) are being trapped.
 *
 *
 * Example 2:
 *
 *
 * Input: height = [4,2,0,3,2,5]
 * Output: 9
 *
 *
 *
 * Constraints:
 *
 *
 * n == height.length
 * 1 <= n <= 2 * 10^4
 * 0 <= height[i] <= 10^5
 *
 *
 */
#include <iostream>
#include <limits>
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
    /**
     * @brief the key insight is that water can only be trapped in valleys, and
     * to quantify any valleys, we can maintain a record of the highest left and
     * right seen elevations.
     *
     * @param height list of elevations for the rain map
     * @return the amount of rain trapped
     */
    int trap(vector<int> &height) {
        auto n = height.size();
        size_t rain = 0, left_elevation = 0, right_elevation = 0;

        // get the max elevation of the entire map
        auto elevation_max = max_element(height.begin(), height.end());
        auto relevation_max = --make_reverse_iterator(elevation_max);
        for (auto it = height.begin(); it != elevation_max; ++it) {
            int elevation = *it;

            // if there is a valley
            if (left_elevation > elevation)
                rain += left_elevation - elevation;
            else
                // record the new max elevation from the left
                left_elevation = elevation;
        }

        for (auto it = height.rbegin(); it != relevation_max; ++it) {
            int elevation = *it;

            // if there is a valley
            if (right_elevation > elevation)
                rain += right_elevation - elevation;
            else
                // record the new max elevation from the right
                right_elevation = elevation;
        }

        return rain;
    }
};
// @lc code=end

int main() {
    // vector<int> arr{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};
    vector<int> arr{4, 2, 0, 3, 2, 5};
    auto ans = Solution().trap(arr);
    std::cout << ans << std::endl;
}
