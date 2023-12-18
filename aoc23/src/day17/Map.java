package day17;

import java.util.Arrays;
import java.util.HashSet;
import java.util.PriorityQueue;
import java.util.Set;

public class Map {
    private int[][] grid;

    private class Node implements Comparable<Node> {
        int x;
        int y;
        int distance;
        int direction;
        int directionCount;

        public Node(int x, int y, int distance, int direction, int directionCount) {
            this.x = x;
            this.y = y;
            this.distance = distance;
            this.direction = direction;
            this.directionCount = directionCount;
        }

        @Override
        public int compareTo(Node o) {
            return this.distance - o.distance;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj)
                return true;
            if (obj == null || getClass() != obj.getClass())
                return false;
            Node node = (Node) obj;
            return x == node.x && y == node.y && distance == node.distance && direction == node.direction
                    && directionCount == node.directionCount;
        }

        public String toString() {
            return y + " " + x + " " + distance + " " + direction + " " + directionCount;
        }
    }

    public Map(String input) {
        String[] lines = input.split("\n");
        grid = new int[lines.length][lines[0].length()];
        for (int y = 0; y < lines.length; y++) {
            String line = lines[y];
            for (int x = 0; x < line.length(); x++) {
                grid[y][x] = Character.getNumericValue(line.charAt(x));
            }
        }
    }

    public int dijkstra() {
        // int[][] distances = new int[grid.length][grid[0].length];
        // for (int y = 0; y < distances.length; y++) {
        //     Arrays.fill(distances[y], Integer.MAX_VALUE);
        // }
        // distances[0][0] = 0;

        Set<Node> visited = new HashSet<Node>();

        PriorityQueue<Node> queue = new PriorityQueue<Node>();
        queue.add(new Node(0, 0, 0, -1, -1));

        while (!queue.isEmpty()) {
            // System.out.println("=====");
            // System.out.println(queue.element());
            Node current = queue.poll();
            // System.out.println(current.y + " " + current.x + " " + current.distance + " "
            // + current.direction + " " + current.directionCount);

            if (visited.contains(current)) {
                continue;
            }

            visited.add(current);

            if (current.y == grid.length - 1 && current.x == grid[0].length - 1) {
                return current.distance;
            }

            int[] dx = { 1, 0, -1, 0 };
            int[] dy = { 0, 1, 0, -1 };
            for (int i = 0; i < dx.length; i++) {
                int newX = current.x + dx[i];
                int newY = current.y + dy[i];
                int newDirection = i;
                int newDirectionCount = current.direction == i ? current.directionCount + 1 : 1;

                if (newY < 0 || newY >= grid.length || newX < 0 || newX >= grid[0].length) {
                    continue;
                }

                // if (visited[newY][newX]) {
                // continue;
                // }

                if (newDirectionCount > 3) {
                    continue;
                }

                if ((newDirection + 2) % 4 == current.direction) {
                    continue;
                }

                int newDistance = current.distance + grid[newY][newX];
                // if (newDistance < distances[newY][newX]) {
                    // distances[newY][newX] = newDistance;
                    Node newNode = new Node(newX, newY, newDistance, newDirection, newDirectionCount);
                    queue.add(newNode);
                    // System.out.println("Added " + newNode);
                    // System.out.println(queue.element());
                // }
            }
        }

        return -1;
    }

    public String toString() {
        String s = "";
        for (int[] row : grid) {
            for (int col : row) {
                s += col;
            }
            s += "\n";
        }
        return s;
    }
}