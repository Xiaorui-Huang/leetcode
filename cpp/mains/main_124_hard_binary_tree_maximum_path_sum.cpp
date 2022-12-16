#include "lc_124_hard_binary_tree_maximum_path_sum.cpp"

#include <iostream>

int main() {
    auto root = build_bt("-10,9,20,null,null,15,7");
    std::cout << root << std::endl;
    auto ans = Solution().maxPathSum(root);
    std::cout << ans << std::endl;
}
