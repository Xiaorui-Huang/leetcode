#include "lc_92_reverse_linked_list_ii.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 92_reverse_linked_list_ii) {
    auto sol = Solution();
    auto head = buildLinkedList(vector{1, 2, 3, 4, 5, 6});
    auto result = linkedListToVector(sol.reverseBetween(head, 2, 4));
    vector<int> expected = vector{1, 4, 3, 2, 5, 6};
    EXPECT_EQ(result, expected);
}

TEST(LeetCode, 92_reverse_linked_list_ii_1) {
    Solution sol;
    auto head = buildLinkedList(vector<int>{7, 8, 9, 10, 11, 12});
    auto result = linkedListToVector(sol.reverseBetween(head, 3, 5));
    vector<int> expected = {7, 8, 11, 10, 9, 12};
    EXPECT_EQ(result, expected);
}

TEST(LeetCode, 92_reverse_linked_list_ii_2) {
    Solution sol;
    auto head = buildLinkedList(vector<int>{7, 8, 9, 10, 11, 12});
    auto result = linkedListToVector(sol.reverseBetween(head, 3, 6));
    vector<int> expected = {7, 8, 12, 11, 10, 9};
    EXPECT_EQ(result, expected);
}

TEST(LeetCode, 92_reverse_linked_list_ii_3) {
    Solution sol;
    auto head = buildLinkedList(vector<int>{7, 8, 9, 10, 11, 12});
    auto result = linkedListToVector(sol.reverseBetween(head, 1, 6));
    vector<int> expected = {12, 11, 10, 9, 8, 7};
    EXPECT_EQ(result, expected);
}

TEST(LeetCode, 92_reverse_linked_list_ii_4) {
    auto sol = Solution();
    auto head = buildLinkedList(vector{1, 2, 3, 4, 5, 6});
    auto result = linkedListToVector(sol.reverseBetween(head, 1, 4));
    vector<int> expected = vector{4, 3, 2, 1, 5, 6};
    EXPECT_EQ(result, expected);
}

TEST(LeetCode, 92_reverse_linked_list_single) {
    auto sol = Solution();
    auto head = buildLinkedList(vector{5});
    auto result = linkedListToVector(sol.reverseBetween(head, 1, 1));
    vector<int> expected = vector{5};
    EXPECT_EQ(result, expected);
}