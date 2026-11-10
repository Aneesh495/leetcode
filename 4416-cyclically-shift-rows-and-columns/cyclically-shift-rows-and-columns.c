#include <stdlib.h>

/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */
int** cyclicShift(int n, int** grid, int gridSize, int* gridColSize, int* rowShift, int rowShiftSize, int* colShift, int colShiftSize, int* returnSize, int** returnColumnSizes) {
    int** result = malloc(gridSize * sizeof(*result));
    *returnSize = gridSize;
    *returnColumnSizes = malloc(gridSize * sizeof(**returnColumnSizes));
    for (int row = 0; row < gridSize; ++row) {
        (*returnColumnSizes)[row] = gridSize;
        result[row] = malloc(gridSize * sizeof(*result[row]));
        for (int col = 0; col < gridSize; ++col) {
            // Undo the column shift first, then undo that source row's shift.
            int sourceRow = (row + colShift[col]) % gridSize;
            int sourceCol = (col + rowShift[sourceRow]) % gridSize;
            result[row][col] = grid[sourceRow][sourceCol];
        }
    }
    return result;
}