import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.LongStream;
import java.util.stream.Stream;

import day05.Category;

public class Day05 {
    private String input;

    public Day05(String input) {
        this.input = input;
    }

    public long partA() {
        String[] maps = input.split("\n\n");
        long[] seeds = Stream.of(maps[0].replace("seeds: ", "").split(" ")).mapToLong(Long::parseLong).toArray();

        List<Category> categories = new ArrayList<Category>();

        for (int i = 1; i < maps.length; i++) {
            categories.add(new Category(maps[i]));
        }

        long lowestLocation = findLowestLocation(seeds, categories);

        return lowestLocation;
    }

    public long partB() {
        String[] maps = input.split("\n\n");
        long[] seeds = Stream.of(maps[0].replace("seeds: ", "").split(" ")).mapToLong(Long::parseLong).toArray();

        List<Category> categories = new ArrayList<Category>();

        for (int i = 1; i < maps.length; i++) {
            categories.add(new Category(maps[i]));
        }

        long lowestLocation = Long.MAX_VALUE;
        for (int i = 0; i < seeds.length; i+=2) {
            long[] seedRange = LongStream.range(seeds[i], seeds[i] + seeds[i + 1]).toArray();
            long rangeLowestLocation = findLowestLocation(seedRange, categories);
            if (rangeLowestLocation < lowestLocation) {
                lowestLocation = rangeLowestLocation;
            }
        }

        return lowestLocation;
    }

    private long findLowestLocation(long[] seeds, List<Category> categories) {
        long lowestLocation = Long.MAX_VALUE;

        for (long seed : seeds) {
            String category = "seed";
            long currentLocation = seed;
            // System.out.println("Seed: " + seed);
            while (!category.equals("location")) {
                String currentCategory = category;
                // System.out.println("Category: " + currentCategory + ", Location: " +
                // currentLocation);
                Category cat = categories.stream().filter(c -> c.getSource().equals(currentCategory)).findFirst().get();
                // System.out.println("Found category: " + cat.getSource() + " " +
                // cat.getDestination());
                currentLocation = cat.getDestination(currentLocation);
                category = cat.getDestination();
                // System.out.println("Category: " + category + ", Location: " + currentLocation
                // + "\n");
            }
            if (currentLocation < lowestLocation) {
                lowestLocation = currentLocation;
            }
        }

        return lowestLocation;
    }
}
