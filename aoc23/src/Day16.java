import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import day16.Beam;
import day16.Contraption;
import day16.Beam.DIRECTION;

public class Day16 {
    private String input;

    public Day16(String input) {
        this.input = input;
    }

    public int partA() {
        Contraption contraption = new Contraption(input);
        Set<String> visited = new HashSet<String>();

        return getEnergized(contraption, 0, 0, DIRECTION.RIGHT, visited);
    }

    public int partB() {
        Contraption contraption = new Contraption(input);

        int maxEnergy = 0;
        for (int x = 0; x < contraption.getWidth(); x++) {
            int top = getEnergized(contraption, x, 0, DIRECTION.DOWN, new HashSet<String>());
            int bottom = getEnergized(contraption, x, contraption.getHeight() - 1, DIRECTION.UP, new HashSet<String>());
            maxEnergy = Math.max(maxEnergy, Math.max(top, bottom));
        }

        for (int y = 0; y < contraption.getHeight(); y++) {
            int left = getEnergized(contraption, 0, y, DIRECTION.RIGHT, new HashSet<String>());
            int right = getEnergized(contraption, contraption.getWidth() - 1, y, DIRECTION.LEFT, new HashSet<String>());
            maxEnergy = Math.max(maxEnergy, Math.max(left, right));
        }

        return maxEnergy;
    }

    private int getEnergized(Contraption contraption, int x, int y, DIRECTION direction, Set<String> visited) {
        List<Beam> beams = Arrays.asList(new Beam(x, y, direction, visited));

        while (beams.size() > 0) {
            beams = getNextBeams(beams, contraption, visited);
        }

        return getEnergizedTiles(visited);
    }

    private List<Beam> getNextBeams(List<Beam> beams, Contraption contraption, Set<String> visited) {
        List<Beam> newBeams = new ArrayList<Beam>();

        for (Beam beam : beams) {
            beam.move(contraption);
            visited.addAll(beam.getPath());
            newBeams.addAll(beam.getSplittedBeams());
        }

        return newBeams;
    }

    private int getEnergizedTiles(Set<String> visited) {
        Set<String> finalSet = new HashSet<String>();

        for (String s : visited) {
            String regex = ".+ (\\(\\d+, \\d+\\))";
            Pattern pattern = Pattern.compile(regex);
            Matcher matcher = pattern.matcher(s);
            if (matcher.find()) {
                finalSet.add(matcher.group(1));
            }
        }

        return finalSet.size();
    }
}
