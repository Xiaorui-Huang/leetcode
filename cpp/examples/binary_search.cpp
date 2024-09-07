
#include <vector>

using namespace std;

int binary_search_left(vector<vector<int>> &nums, int target, int pos) {
    int lo = 0, hi = nums.size() - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int num = nums[mid][pos];
        if (num <= target) {
            lo = mid + 1;
        } else {
            hi = mid - 1;
        }
    }
    return hi; // -1 return
}

// min position larger than target
int binary_search_right(vector<vector<int>> &nums, int target) {
    int lo = 0, hi = nums.size() - 1;

    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        int num = nums[mid][0];
        if (target <= num) {
            hi = mid - 1;
        } else {
            lo = mid + 1;
        }
    }
    return lo; // n return
}