#include <stdbool.h>

bool checkGoodInteger(int n) {
    int difference = 0;
    for (; n > 0; n /= 10) {
        int digit = n % 10;
        difference += digit * (digit - 1);
    }
    return difference >= 50;
}