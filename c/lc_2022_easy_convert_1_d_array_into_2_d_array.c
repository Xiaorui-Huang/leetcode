/*
 * @lc app=leetcode id=2022 lang=c
 *
 * [2022] Convert 1D Array Into 2D Array
 *
 * https://leetcode.com/problems/convert-1d-array-into-2d-array/description/
 *
 * algorithms
 * Easy (61.01%)
 * Likes:    926
 * Dislikes: 66
 * Total Accepted:    130.6K
 * Total Submissions: 195.4K
 * Testcase Example:  '[1,2,3,4]\n2\n2'
 *
 * You are given a 0-indexed 1-dimensional (1D) integer array original, and two
 * integers, m and n. You are tasked with creating a 2-dimensional (2D) array
 * with  m rows and n columns using all the elements from original.
 * 
 * The elements from indices 0 to n - 1 (inclusive) of original should form the
 * first row of the constructed 2D array, the elements from indices n to 2 * n
 * - 1 (inclusive) should form the second row of the constructed 2D array, and
 * so on.
 * 
 * Return an m x n 2D array constructed according to the above procedure, or an
 * empty 2D array if it is impossible.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: original = [1,2,3,4], m = 2, n = 2
 * Output: [[1,2],[3,4]]
 * Explanation: The constructed 2D array should contain 2 rows and 2 columns.
 * The first group of n=2 elements in original, [1,2], becomes the first row in
 * the constructed 2D array.
 * The second group of n=2 elements in original, [3,4], becomes the second row
 * in the constructed 2D array.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: original = [1,2,3], m = 1, n = 3
 * Output: [[1,2,3]]
 * Explanation: The constructed 2D array should contain 1 row and 3 columns.
 * Put all three elements in original into the first row of the constructed 2D
 * array.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: original = [1,2], m = 1, n = 1
 * Output: []
 * Explanation: There are 2 elements in original.
 * It is impossible to fit 2 elements in a 1x1 2D array, so return an empty 2D
 * array.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= original.length <= 5 * 10^4
 * 1 <= original[i] <= 10^5
 * 1 <= m, n <= 4 * 10^4
 * 
 * 
 */

// @lc code=start
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** construct2DArray(int* original, int originalSize, int m, int n, int* returnSize, int** returnColumnSizes) {
    if(m * n != originalSize){
        *returnSize = 0;
        return (int **)malloc(0);
    }
    // prep the return metas
    *returnSize = m;
    int * colsizes = (int *) malloc(sizeof(int) * m);
    for (int i = 0; i < m; i++)
        colsizes[i] = n;
    *returnColumnSizes = colsizes;

    int counter = 0;
    int ** matrix = (int **) malloc(sizeof(int *) * m);
    for (int i = 0; i < m; i++){
        matrix[i] = (int *) malloc(sizeof(int) * n);
        for (int j = 0; j < n; j++)
            matrix[i][j] = original[counter++];
    }
    
    return matrix;
}
// @lc code=end

