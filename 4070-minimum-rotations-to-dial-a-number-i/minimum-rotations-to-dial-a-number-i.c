int minRotations(char* s) {
    int previous = 0, total = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        int digit = s[i] - '0';
        int difference = digit - previous;
        if (difference < 0) difference = -difference;
        // The clockwise and counterclockwise distances add up to ten.
        total += difference < 10 - difference ? difference : 10 - difference;
        previous = digit;
    }
    return total;
}