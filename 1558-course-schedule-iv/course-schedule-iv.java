import java.util.ArrayList;
import java.util.BitSet;
import java.util.List;

class Solution {
    public List<Boolean> checkIfPrerequisite(int numCourses, int[][] prerequisites, int[][] queries) {
        BitSet[] reachable = new BitSet[numCourses];
        for (int course = 0; course < numCourses; course++) {
            reachable[course] = new BitSet(numCourses);
        }
        for (int[] edge : prerequisites) {
            reachable[edge[0]].set(edge[1]);
        }

        // Floyd-Warshall transitive closure, merging a whole row at once.
        for (int via = 0; via < numCourses; via++) {
            for (int from = 0; from < numCourses; from++) {
                if (reachable[from].get(via)) {
                    reachable[from].or(reachable[via]);
                }
            }
        }

        List<Boolean> answers = new ArrayList<>(queries.length);
        for (int[] query : queries) {
            answers.add(reachable[query[0]].get(query[1]));
        }
        return answers;
    }
}