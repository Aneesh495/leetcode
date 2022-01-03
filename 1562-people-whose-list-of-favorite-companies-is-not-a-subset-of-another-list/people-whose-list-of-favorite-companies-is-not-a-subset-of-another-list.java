class Solution {
    public List<Integer> peopleIndexes(List<List<String>> favoriteCompanies) {
        int n = favoriteCompanies.size();
        List<Set<String>> sets = new ArrayList<>();
        for (List<String> list : favoriteCompanies) sets.add(new HashSet<>(list));
        List<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            boolean subset = false;
            for (int j = 0; j < n; j++) {
                if (i != j && sets.get(j).containsAll(sets.get(i))) { subset = true; break; }
            }
            if (!subset) answer.add(i);
        }
        return answer;
    }
}