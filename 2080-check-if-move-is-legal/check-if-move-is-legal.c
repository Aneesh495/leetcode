#include <stdbool.h>

bool checkMove(char** board, int boardSize, int* boardColSize, int rMove, int cMove, char color) {
    const char opposite = color == 'W' ? 'B' : 'W';
    for (int dr = -1; dr <= 1; ++dr) {
        for (int dc = -1; dc <= 1; ++dc) {
            if (dr == 0 && dc == 0) continue;
            int row = rMove + dr;
            int col = cMove + dc;
            int captured = 0;

            // Scan a ray of opposing pieces until it ends or leaves the board.
            while (row >= 0 && row < boardSize && col >= 0 && col < boardColSize[row]) {
                if (board[row][col] == color && captured > 0) return true;
                if (board[row][col] != opposite) break;
                ++captured;
                row += dr;
                col += dc;
            }
        }
    }
    return false;
}