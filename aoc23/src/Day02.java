import java.util.ArrayList;
import java.util.List;
import java.util.stream.IntStream;

import day02.Game;

public class Day02 {
    private String input;
    private int possibleRed = 12;
    private int possibleGreen = 13;
    private int possibleBlue = 14;

    public Day02(String input) {
        this.input = input;
    }

    public int partA() {
        Game[] games = parseGames();
        int[] possibleGameIds = possibleGameIds(games);
        int sum = IntStream.of(possibleGameIds).sum();

        return sum;
    }

    public int partB() {
        Game[] games = parseGames();
        int[] powerPerGame = getPowerPerGame(games);
        int power = IntStream.of(powerPerGame).sum();

        return power;
    }

    private int[] getPowerPerGame(Game[] games) {
        int[] powerPerGame = new int[games.length];
        for (int i = 0; i < games.length; i++) {
            int maxRed = games[i].getMax("red");
            int maxGreen = games[i].getMax("green");
            int maxBlue = games[i].getMax("blue");

            powerPerGame[i] = maxRed * maxGreen * maxBlue;
        }

        return powerPerGame;
    }

    private int[] possibleGameIds(Game[] games) {
        List<Integer> possibleGameIds = new ArrayList<Integer>();
        for (Game game : games) {
            int maxRed = game.getMax("red");
            int maxGreen = game.getMax("green");
            int maxBlue = game.getMax("blue");

            if (maxRed <= possibleRed && maxGreen <= possibleGreen && maxBlue <= possibleBlue) {
                possibleGameIds.add(game.getId());
            }
        }

        return possibleGameIds.stream().mapToInt(Integer::intValue).toArray();
    }

    private Game[] parseGames() {
        String[] lines = input.split("\n");
        Game[] games = new Game[lines.length];
        for (int i = 0; i < lines.length; i++) {
            String[] gameTokens = lines[i].split(":");
            int gameId = Integer.parseInt(gameTokens[0].replace("Game ", ""));
            Game game = new Game(gameId);
            String[] grabs = gameTokens[1].split(";");
            for (String grab : grabs) {
                String[] cubes = grab.split(",");
                int red = 0, green = 0, blue = 0;
                for (String cube : cubes) {
                    String[] cubeTokens = cube.trim().split(" ");
                    int amount = Integer.parseInt(cubeTokens[0]);
                    String color = cubeTokens[1];
                    switch (color) {
                        case "red":
                            red = amount;
                            break;
                        case "green":
                            green = amount;
                            break;
                        case "blue":
                            blue = amount;
                            break;
                        default:
                            break;
                    }
                }
                game.addRecord(red, green, blue);
            }
            games[i] = game;
        }

        return games;
    }
}