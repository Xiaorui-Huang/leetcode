/*
 * @lc app=leetcode id=2326 lang=c
 *
 * [2326] Spiral Matrix IV
 *
 * https://leetcode.com/problems/spiral-matrix-iv/description/
 *
 * algorithms
 * Medium (75.90%)
 * Likes:    799
 * Dislikes: 29
 * Total Accepted:    50.9K
 * Total Submissions: 66.5K
 * Testcase Example:  '3\n5\n[3,0,2,6,8,1,7,9,4,2,5,5,0]'
 *
 * You are given two integers m and n, which represent the dimensions of a
 * matrix.
 * 
 * You are also given the head of a linked list of integers.
 * 
 * Generate an m x n matrix that contains the integers in the linked list
 * presented in spiral order (clockwise), starting from the top-left of the
 * matrix. If there are remaining empty spaces, fill them with -1.
 * 
 * Return the generated matrix.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: m = 3, n = 5, head = [3,0,2,6,8,1,7,9,4,2,5,5,0]
 * Output: [[3,0,2,6,8],[5,0,-1,-1,1],[5,2,4,9,7]]
 * Explanation: The diagram above shows how the values are printed in the
 * matrix.
 * Note that the remaining spaces in the matrix are filled with -1.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: m = 1, n = 4, head = [0,1,2]
 * Output: [[0,1,2,-1]]
 * Explanation: The diagram above shows how the values are printed from left to
 * right in the matrix.
 * The last space in the matrix is set to -1.
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= m, n <= 10^5
 * 1 <= m * n <= 10^5
 * The number of nodes in the list is in the range [1, m * n].
 * 0 <= Node.val <= 1000
 * 
 * 
 */


#include <stdlib.h>
#include <string.h>

// Definition for singly-linked list.
struct ListNode {
    int val;
    struct ListNode *next;
};
// Return an array of arrays of size *returnSize.
// The sizes of the arrays are returned as *returnColumnSizes array.
// Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().

// @lc code=start
inline void swap(int *a, int *b){
    int temp = *a;
    *a = *b;
    *b = temp;
}

int** spiralMatrix(int m, int n, struct ListNode* head, int* returnSize, int** returnColumnSizes) {
    *returnSize = m;
    *returnColumnSizes = (int*)malloc(m * sizeof(int));
    for (int i = 0; i < m; i++) 
        (*returnColumnSizes)[i] = n;

    int** matrix = (int**)malloc(m * sizeof(int*));
    for (int i = 0; i < m; i++) {
        matrix[i] = (int*)malloc(n * sizeof(int));
        // not safe by any means
        memset(matrix[i], 0xFF, n * sizeof(int)); // 0xFF is the two's compliment, which represents -1 in most systems
    }

    int top = 0, bottom = m - 1, left = 0, right = n - 1;

    while (head != NULL) {
        for (int col = left; col <= right && head != NULL; col++) {
            matrix[top][col] = head->val;
            head = head->next;
        }
        top++;

        for (int row = top; row <= bottom && head != NULL; row++) {
            matrix[row][right] = head->val;
            head = head->next;
        }
        right--;

        for (int col = right; col >= left && head != NULL; col--) {
            matrix[bottom][col] = head->val;
            head = head->next;
        }
        bottom--;

        for (int row = bottom; row >= top && head != NULL; row--) {
            matrix[row][left] = head->val;
            head = head->next;
        }
        left++;
    }

    return matrix;
}
/**
 * @brief  My original thought-ish 
 * int** spiralMatrix(int m, int n, struct ListNode* head, int* returnSize, int** returnColumnSizes) {
    
    int **ans = (int **)malloc(sizeof(int *) * m);

    *returnSize = m;
    *returnColumnSizes = (int *)malloc(sizeof(int) * m);

    for (int i = 0; i < m; i++) {
        ans[i] = (int *)calloc(1, sizeof(int) * n);
        (*returnColumnSizes)[i] = n;
    }

    for (int x = 0, y = 0, dir = 0, cnt = m * n, top = 0, bottom = m, left = 0, right = n; cnt; cnt--) {
        if (head) {
            ans[x][y] = head->val;
            head = head->next;
        }
        else {
            ans[x][y] = -1;
        }

        // Right 
        if (dir == 0) {
            if (y + 1 == right) {
                dir = 1;
                x++;
                top++;
            }
            else {
                y++;
            }
        }
        // Down
        else if (dir == 1) {
            if (x + 1 == bottom) {
                dir = 2;
                y--;
                right--;
            }
            else {
                x++;
            }
        }
        // Left 
        else if (dir == 2) {
            if (y - 1 < left) {
                dir = 3;;
                x--;
                bottom--;
            }
            else {
                y--;
            }
        }
        // Up 
        else {
            if (x - 1 < top) {
                dir = 0;
                y++;
                left++;
            }
            else {
                x--;
            }
        }
    }

    return ans;
}
 * 
 */
// @lc code=end

