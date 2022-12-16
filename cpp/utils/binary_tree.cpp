/**
 * Original Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
#include "binary_tree.h"
#include <queue>

using std::string;
using std::vector;
// Enable to print vectors just by calling its name

std::tuple<std::vector<string>, int, int, int> TreeNode::display_aux() {
    int width, height, middle;
    string s = std::to_string(val);
    int u = s.length();

    if (!right && !left) {
        std::vector<string> lines;
        lines.emplace_back(s);
        width = u;
        height = 1;
        middle = width / 2;
        return std::make_tuple(lines, width, height, middle);
    }

    if (!right) {
        auto [lines, n, p, x] = left->display_aux();
        string first_line = string(x + 1, ' ') + string(n - x - 1, '_') + s;
        string second_line = string(x, ' ') + '/' + string(n - x - 1 + u, ' ');

        std::vector<string> shifted_lines;
        for (auto &&line : lines)
            shifted_lines.emplace_back(line + string(u, ' '));

        shifted_lines.emplace(shifted_lines.begin(), second_line);
        shifted_lines.emplace(shifted_lines.begin(), first_line);
        return std::make_tuple(shifted_lines, n + u, p + 2, n + u / 2);
    }

    if (!left) {
        auto [lines, n, p, x] = right->display_aux();
        string first_line = s + string(x, '_') + string(n - x, ' ');
        string second_line = string(u + x, ' ') + '\\' + string(n - x - 1, ' ');

        std::vector<string> shifted_lines;
        for (auto &&line : lines)
            shifted_lines.emplace_back(string(u, ' ') + line);

        shifted_lines.emplace(shifted_lines.begin(), second_line);
        shifted_lines.emplace(shifted_lines.begin(), first_line);
        return std::make_tuple(shifted_lines, n + u, p + 2, u / 2);
    }

    std::vector<string> lines;
    auto [left_lines, n, p, x] = left->display_aux();
    auto [right_lines, m, q, y] = right->display_aux();
    string first_line = string(x + 1, ' ') + string(n - x - 1, '_') + s + string(y, '_') + string(m - y, ' ');
    string second_line = string(x, ' ') + '/' + string(n - x - 1 + u + y, ' ') + "\\" + string(m - y - 1, ' ');
    if (p < q)
        for (size_t i = 0; i < q - p; i++)
            left_lines.emplace_back(string(n, ' '));
    else if (q < p)
        for (size_t i = 0; i < p - q; i++)
            right_lines.emplace_back(string(m, ' '));

    int l = std::min(left_lines.size(), right_lines.size());
    lines.reserve(l);
    for (size_t i = 0; i < l; i++)
        lines.emplace_back(left_lines[i] + string(u, ' ') + right_lines[i]);
    lines.emplace(lines.begin(), second_line);
    lines.emplace(lines.begin(), first_line);
    return std::make_tuple(lines, n + m + u, std::max(p, q) + 2, n + u / 2);
}

std::vector<int *> parse_leetcode_bt(string s, char del) {
    std::vector<int *> node_list;
    std::stringstream ss(s);
    string word;
    int *pt;
    while (!ss.eof()) {
        getline(ss, word, del);
        if (word == "null")
            node_list.emplace_back(nullptr);
        else
            node_list.emplace_back(new int(stoi(word)));
    }
    return node_list;
}

/**
 * @brief Create a TreeNode from LeetCode list convention format of int or null_ptr
 *
 * @param node_list
 * @return TreeNode *
 */
TreeNode *build_bt(std::vector<int *> node_list) {
    auto n = node_list.size();
    if (n == 0)
        return nullptr;
    auto root = new TreeNode(*node_list[0]);

    std::queue<TreeNode *> q;
    q.push(root);
    size_t index = 1;

    while (index < n) {
        auto cur = q.front();
        q.pop();
        int *left_val_pt = node_list[index];
        int *right_val_pt = (index + 1 < n) ? node_list[index + 1] : nullptr;

        if (left_val_pt) {
            auto left_node = new TreeNode(*left_val_pt);
            cur->left = left_node;
            q.push(cur->left);
        }
        if (right_val_pt) {
            auto right_node = new TreeNode(*right_val_pt);
            cur->right = right_node;
            q.push(cur->right);
        }
        index += 2;
    }
    return root;
}

TreeNode *build_bt(string leetcode_bt) { return build_bt(parse_leetcode_bt(leetcode_bt)); }

std::ostream &operator<<(std::ostream &output, TreeNode &root) {
    auto [lines, _1, _2, _3] = root.display_aux();
    for (auto &&line : lines)
        output << line << "\n";
    return output;
}

std::ostream &operator<<(std::ostream &output, TreeNode *&root) {
    auto [lines, _1, _2, _3] = root->display_aux();
    for (auto &&line : lines)
        output << line << "\n";
    return output;
}