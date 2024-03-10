#include "lc_232_easy_implement_queue_using_stacks.cpp"
#include <gtest/gtest.h>

TEST(LeetCode, 232_easy_implement_queue_using_stacks) {

    MyQueue *q = new MyQueue();
    EXPECT_TRUE(q->empty());

    q->push(1);
    EXPECT_EQ(q->peek(), 1);
    EXPECT_EQ(q->pop(), 1);

    q->push(2);
    q->push(3);
    EXPECT_EQ(q->peek(), 2);
    EXPECT_FALSE(q->empty());

    EXPECT_EQ(q->pop(), 2);
    EXPECT_EQ(q->pop(), 3);
}