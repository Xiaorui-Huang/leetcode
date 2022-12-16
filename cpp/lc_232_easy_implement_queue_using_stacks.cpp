#ifndef LC_232_EASY_IMPLEMENT_QUEUE_USING_STACKS_H
#define LC_232_EASY_IMPLEMENT_QUEUE_USING_STACKS_H
/*
 * @lc app=leetcode id=232 lang=cpp
 *
 * [232] Implement Queue using Stacks
 *
 * https://leetcode.com/problems/implement-queue-using-stacks/description/
 *
 * algorithms
 * Easy (61.40%)
 * Likes:    4786
 * Dislikes: 306
 * Total Accepted:    549K
 * Total Submissions: 891.1K
 * Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
 *
 * Implement a first in first out (FIFO) queue using only two stacks. The
 * implemented queue should support all the functions of a normal queue (push,
 * peek, pop, and empty).
 *
 * Implement the MyQueue class:
 *
 *
 * void push(int x) Pushes element x to the back of the queue.
 * int pop() Removes the element from the front of the queue and returns
 * it.
 * int peek() Returns the element at the front of the queue.
 * boolean empty() Returns true if the queue is empty, false otherwise.
 *
 *
 * Notes:
 *
 *
 * You must use only standard operations of a stack, which means only push to
 * top, peek/pop from top, size, and is empty operations are valid.
 * Depending on your language, the stack may not be supported natively. You may
 * simulate a stack using a list or deque (double-ended queue) as long as you
 * use only a stack's standard operations.
 *
 *
 *
 * Example 1:
 *
 *
 * Input
 * ["MyQueue", "push", "push", "peek", "pop", "empty"]
 * [[], [1], [2], [], [], []]
 * Output
 * [null, null, null, 1, 1, false]
 *
 * Explanation
 * MyQueue myQueue = new MyQueue();
 * myQueue.push(1); // queue is: [1]
 * myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
 * myQueue.peek(); // return 1
 * myQueue.pop(); // return 1, queue is [2]
 * myQueue.empty(); // return false
 *
 *
 *
 * Constraints:
 *
 *
 * 1 <= x <= 9
 * At most 100 calls will be made to push, pop, peek, and empty.
 * All the calls to pop and peek are valid.
 *
 *
 *
 * Follow-up: Can you implement the queue such that each operation is amortized
 * O(1) time complexity? In other words, performing n operations will take
 * overall O(n) time even if one of those operations may take longer.
 *
 */

#include <stack>
using namespace std;
// Enable to print vectors just by calling its name
template <typename S> ostream &operator<<(ostream &os, const vector<S> &vector) {
    for (auto element : vector)
        os << element << " ";
    return os;
}
// @lc code=start
class MyQueue {
  public:
    stack<int> in, out;
    int cache;
    MyQueue() {
        in = stack<int>();
        out = stack<int>();
    }

    void push(int x) {
        if (in.empty())
            cache = x;
        in.push(x);
    }

    int pop() {
        if (empty())
            throw "Cannot pop empty queue";
        if (!out.empty())
            return pop_val(out);

        while (!in.empty())
            out.push(pop_val(in));

        return pop_val(out);
    }

    int peek() {
        if (!out.empty())
            return out.top();
        if (empty())
            throw "Cannot peek empty queue";
        return cache;
    }

    bool empty() { return size() == 0; }
    int size() { return in.size() + out.size(); }

  private:
    int pop_val(stack<int> &stack) {
        auto top = stack.top();
        stack.pop();
        return top;
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
// @lc code=end
#endif
