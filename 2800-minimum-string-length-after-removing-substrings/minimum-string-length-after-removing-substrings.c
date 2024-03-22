int minLength(char* s) {
    char stack[100];
    int size = 0;
    for (int i = 0; s[i] != '\0'; ++i) {
        // A deletion can only create a new candidate at the current stack boundary.
        if (size > 0 && ((stack[size - 1] == 'A' && s[i] == 'B') ||
                         (stack[size - 1] == 'C' && s[i] == 'D'))) {
            --size;
        } else {
            stack[size++] = s[i];
        }
    }
    return size;
}