import java.util.*;

class FoodRatings {
    private static class Entry {
        String food;
        int rating;
        Entry(String food, int rating) { this.food = food; this.rating = rating; }
    }

    private Map<String, Integer> ratingsByFood = new HashMap<>();
    private Map<String, String> cuisineByFood = new HashMap<>();
    private Map<String, PriorityQueue<Entry>> heaps = new HashMap<>();

    private PriorityQueue<Entry> newHeap() {
        return new PriorityQueue<>((a, b) -> {
            if (a.rating != b.rating) return Integer.compare(b.rating, a.rating);
            return a.food.compareTo(b.food);
        });
    }

    public FoodRatings(String[] foods, String[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.length; i++) {
            ratingsByFood.put(foods[i], ratings[i]);
            cuisineByFood.put(foods[i], cuisines[i]);
            heaps.computeIfAbsent(cuisines[i], k -> newHeap()).offer(new Entry(foods[i], ratings[i]));
        }
    }

    public void changeRating(String food, int newRating) {
        ratingsByFood.put(food, newRating);
        heaps.get(cuisineByFood.get(food)).offer(new Entry(food, newRating));
    }

    public String highestRated(String cuisine) {
        PriorityQueue<Entry> heap = heaps.get(cuisine);
        while (heap.peek().rating != ratingsByFood.get(heap.peek().food)) heap.poll();
        return heap.peek().food;
    }
}