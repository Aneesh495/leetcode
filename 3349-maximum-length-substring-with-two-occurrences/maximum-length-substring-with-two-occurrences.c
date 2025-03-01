int maximumLengthSubstring(char* s) {
    int frequency[26] = {0};
    int left = 0;
    int best = 0;
    for (int right = 0; s[right] != '\0'; right++) {
        int current = s[right] - 'a';
        frequency[current]++;
        while (frequency[current] > 2) {
            frequency[s[left] - 'a']--;
            left++;
        }
        int length = right - left + 1;
        if (length > best) best = length;
    }
    return best;
}