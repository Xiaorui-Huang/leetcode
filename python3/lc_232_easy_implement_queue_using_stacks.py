#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#
# https://leetcode.com/problems/implement-queue-using-stacks/description/
#
# algorithms
# Easy (61.40%)
# Likes:    4786
# Dislikes: 306
# Total Accepted:    549K
# Total Submissions: 891.1K
# Testcase Example:  '["MyQueue","push","push","peek","pop","empty"]\n[[],[1],[2],[],[],[]]'
#
# Implement a first in first out (FIFO) queue using only two stacks. The
# implemented queue should support all the functions of a normal queue (push,
# peek, pop, and empty).
#
# Implement the MyQueue class:
#
#
# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
#
#
# Notes:
#
#
# You must use only standard operations of a stack, which means only push to
# top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may
# simulate a stack using a list or deque (double-ended queue) as long as you
# use only a stack's standard operations.
#
#
#
# Example 1:
#
#
# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]
#
# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
#
#
#
# Constraints:
#
#
# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
#
#
#
# Follow-up: Can you implement the queue such that each operation is amortized
# O(1) time complexity? In other words, performing n operations will take
# overall O(n) time even if one of those operations may take longer.
#
#

# @lc code=start
# Amortized O(1) for pop and O(1) for push
class MyQueue:
    def __init__(self) -> None:
        self.in_stack: list[int] = []
        self.out_stack: list[int] = []
        self.cache: int

    def push(self, x: int) -> None:
        # record the first value entering the queue as cache for peek
        if not self.in_stack:
            self.cache = x
        self.in_stack.append(x)

    def pop(self) -> int:
        # validation
        if self.empty():
            raise Exception("Cannot pop an empty queue")

        # this is what makes it aromatized O(1)
        if self.out_stack:
            return self.out_stack.pop()

        # pop out all values to out stack, where the values are now from oldest to newest
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()  # extract the oldest value

    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]  # using stack.peek operation

        if self.empty():
            raise Exception("Cannot peek an empty queue")

        return self.cache

    def empty(self) -> bool:
        return not len(self)

    def __len__(self) -> int:
        return len(self.in_stack) + len(self.out_stack)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
