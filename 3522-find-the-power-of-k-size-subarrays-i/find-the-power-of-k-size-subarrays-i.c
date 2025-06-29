int* resultsArray(int* nums, int numsSize, int k, int* returnSize) {
    *returnSize = numsSize - k + 1;
    int* answer = (int*)malloc((*returnSize) * sizeof(int));
    int streak = 1;
    for (int i = 0; i < numsSize; ++i) {
        if (i > 0 && nums[i] == nums[i - 1] + 1) streak++;
        else streak = 1;
        if (i >= k - 1) answer[i - k + 1] = (streak >= k ? nums[i] : -1);
    }
    return answer;
}