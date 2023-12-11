package day11;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Universe {
    private Set<Integer> occupiedRows;
    private Set<Integer> occupiedColumns;
    private List<Galaxy> galaxies;
    private int expansionFactor;

    public Universe(String input, int expansionFactor) {
        occupiedRows = new HashSet<Integer>();
        occupiedColumns = new HashSet<Integer>();
        galaxies = new ArrayList<Galaxy>();

        int id = 1;
        String[] rows = input.split("\n");
        for (int i = 0; i < rows.length; i++) {
            String[] columns = rows[i].split("");
            for (int j = 0; j < columns.length; j++) {
                if (columns[j].equals("#")) {
                    this.occupiedRows.add(i);
                    this.occupiedColumns.add(j);
                    this.galaxies.add(new Galaxy(id, i, j));
                    // System.out.println(String.format("%d, %d, %d", id, i, j));
                    id++;
                }
            }
        }

        if (expansionFactor == 1) {
            this.expansionFactor = 1;
        } else {
            this.expansionFactor = expansionFactor - 1;
        }
    }

    public long calculateDistance() {
        long sum = 0;
        for (int i = 0; i < galaxies.size(); i++) {
            for (int j = i + 1; j < galaxies.size(); j++) {
                // System.out.println(String.format("%d, %d", i, j));
                sum += calculateDistance(galaxies.get(i), galaxies.get(j));
            }
        }
        return sum;
    }

    public long calculateDistance(Galaxy galaxy1, Galaxy galaxy2) {
        int minRow = Math.min(galaxy1.getRow(), galaxy2.getRow());
        int maxRow = Math.max(galaxy1.getRow(), galaxy2.getRow());
        Set<Integer> rowRange = IntStream.range(minRow, maxRow + 1).boxed().collect(Collectors.toSet());

        int minColumn = Math.min(galaxy1.getColumn(), galaxy2.getColumn());
        int maxColumn = Math.max(galaxy1.getColumn(), galaxy2.getColumn());
        Set<Integer> columnRange = IntStream.range(minColumn, maxColumn + 1).boxed().collect(Collectors.toSet());

        // System.out.println(String.format("(%d %d %d %d)", minRow, maxRow, minColumn,
        // maxColumn));
        // System.out.println(rowRange.toString() + " " + columnRange.toString());

        rowRange.removeAll(occupiedRows);
        columnRange.removeAll(occupiedColumns);

        // System.out.println(rowRange.toString() + " " + columnRange.toString());

        int manhattanDistance = Math.abs(maxRow - minRow) + Math.abs(maxColumn - minColumn);
        // System.out.println(String.format("%d, %d, %d, %d", minRow, maxRow, minColumn,
        // maxColumn));
        // System.out.println(galaxy1.toString() + " " + galaxy2.toString() + " " +
        // manhattanDistance);
        long totalDistance = manhattanDistance + (rowRange.size() * this.expansionFactor) + (columnRange.size() * this.expansionFactor);

        // System.out.println(galaxy1.toString() + " " + galaxy2.toString() + " " +
        // totalDistance);

        return totalDistance;
    }

    public String toString() {
        StringBuilder sb = new StringBuilder();

        for (Galaxy galaxy : galaxies) {
            sb.append(galaxy.toString());
        }

        sb.append("\nOccupied rows: " + occupiedRows.toString() + "\n");
        sb.append("Occupied columns: " + occupiedColumns.toString());

        return sb.toString();
    }
}
