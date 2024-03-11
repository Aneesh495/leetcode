class Solution {
    public int[] colorTheArray(int n, int[][] queries) {
        int[] colors = new int[n];
        int[] answer = new int[queries.length];
        int same = 0;
        for (int q = 0; q < queries.length; ++q) {
            int index = queries[q][0], color = queries[q][1];
            int old = colors[index];
            if (old != 0) {
                if (index > 0 && colors[index - 1] == old) --same;
                if (index + 1 < n && colors[index + 1] == old) --same;
            }
            colors[index] = color;
            if (index > 0 && colors[index - 1] == color) ++same;
            if (index + 1 < n && colors[index + 1] == color) ++same;
            answer[q] = same;
        }
        return answer;
    }
}