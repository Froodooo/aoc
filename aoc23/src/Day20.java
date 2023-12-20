import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Queue;
import java.util.Set;

import day20.ConjunctionModule;
import day20.DefaultModule;
import day20.FlipFlopModule;
import day20.Message;
import day20.Module;
import day20.Message.Pulse;

public class Day20 {
    private String input;

    public Day20(String input) {
        this.input = input;
    }

    public int partA() {
        Map<String, Module> modules = parseInput(input);
        Queue<Message> queue = new ArrayDeque<Message>();

        int lowPulses = 0;
        int highPulses = 0;

        for (int i = 0; i < 1000; i++) {
            queue.add(new Message(Pulse.LOW, "start", "broadcaster"));

            while (!queue.isEmpty()) {
                Message message = queue.poll();
                if (message.getPulse() == Pulse.LOW) {
                    lowPulses++;
                } else {
                    highPulses++;
                }
                Module module = modules.get(message.getReceiver());
                List<Message> newMessages = module.handleMessage(message);
                queue.addAll(newMessages);
            }
        }

        return lowPulses * highPulses;
    }

    public long partB() {
        Map<String, Module> modules = parseInput(input);
        Queue<Message> queue = new ArrayDeque<Message>();

        // If all of the following modules are low,
        // a high signal is sent to module qb,
        // which in turn sends a low signal to rx.
        // The modules below are probably different for other people.
        long kv = -1;
        long jg = -1;
        long rz = -1;
        long mr = -1;

        long count = 0;

        while (kv == -1 || jg == -1 || rz == -1 || mr == -1) {
            queue.add(new Message(Pulse.LOW, "start", "broadcaster"));

            while (!queue.isEmpty()) {
                Message message = queue.poll();
                if (message.getReceiver().equals("kv") && message.getPulse() == Pulse.LOW && kv < 0) {
                    kv = 0;
                }
                if (message.getReceiver().equals("jg") && message.getPulse() == Pulse.LOW && jg < 0) {
                    jg = 0;
                }
                if (message.getReceiver().equals("rz") && message.getPulse() == Pulse.LOW && rz < 0) {
                    rz = 0;
                }
                if (message.getReceiver().equals("mr") && message.getPulse() == Pulse.LOW && mr < 0) {
                    mr = 0;
                }
                Module module = modules.get(message.getReceiver());
                List<Message> newMessages = module.handleMessage(message);
                queue.addAll(newMessages);
            }

            count++;

            if (kv == 0) {
                kv = count;
            }
            if (jg == 0) {
                jg = count;
            }
            if (rz == 0) {
                rz = count;
            }
            if (mr == 0) {
                mr = count;
            }
        }

        return lcm(kv, lcm(jg, lcm(rz, mr)));
    }

    // https://www.baeldung.com/java-least-common-multiple
    private long lcm(long number1, long number2) {
        if (number1 == 0 || number2 == 0) {
            return 0;
        }
        long absNumber1 = Math.abs(number1);
        long absNumber2 = Math.abs(number2);
        long absHigherNumber = Math.max(absNumber1, absNumber2);
        long absLowerNumber = Math.min(absNumber1, absNumber2);
        long lcm = absHigherNumber;
        while (lcm % absLowerNumber != 0) {
            lcm += absHigherNumber;
        }
        return lcm;
    }

    private Map<String, Module> parseInput(String input) {
        Set<String> moduleNames = new HashSet<>();
        Map<String, Module> modules = new HashMap<>();
        Map<String, List<String>> in = new HashMap<>();
        Map<String, List<String>> out = new HashMap<>();
        String[] lines = input.split("\n");
        for (String line : lines) {
            String[] parts = line.split("->");
            String sender = parts[0].trim();
            String[] receivers = parts[1].trim().split(", ");
            updateModuleNames(moduleNames, sender, receivers);
            updateIn(in, sender, receivers);
            updateOut(out, sender, receivers);
        }

        for (String sender : moduleNames) {
            String[] outs = out.getOrDefault(sender, new ArrayList<String>())
                    .toArray(new String[out.getOrDefault(sender, new ArrayList<String>()).size()]);
            if (sender.startsWith("%")) {
                String name = sender.replace("%", "");
                modules.put(name, new FlipFlopModule(name, outs));
            } else if (sender.startsWith("&")) {
                String name = sender.replace("&", "");
                String[] ins = in.get(name).toArray(new String[in.get(name).size()]);
                modules.put(name, new ConjunctionModule(name, outs, ins));
            } else {
                String name = sender;
                modules.put(name, new DefaultModule(name, outs));
            }
        }

        return modules;
    }

    private void updateModuleNames(Set<String> moduleNames, String sender, String[] receivers) {
        if (moduleNames.contains(sender.replaceAll("[&%]", "")) && !sender.equals("broadcaster")) {
            moduleNames.remove(sender.replaceAll("[&%]", ""));
            moduleNames.add(sender);
        } else if (!moduleNames.contains("%" + sender) && !moduleNames.contains("&" + sender)) {
            moduleNames.add(sender);
        }

        for (String receiver : receivers) {
            if (moduleNames.contains(receiver.replaceAll("[&%]", ""))) {
                moduleNames.remove(receiver.replaceAll("[&%]", ""));
                moduleNames.add(receiver);
            } else if (!moduleNames.contains("%" + receiver) && !moduleNames.contains("&" + receiver)) {
                moduleNames.add(receiver);
            }
        }
    }

    private void updateIn(Map<String, List<String>> in, String sender, String[] receivers) {
        for (String receiver : receivers) {
            if (in.containsKey(receiver)) {
                in.get(receiver).add(sender);
            } else {
                in.put(receiver, new ArrayList<String>(Arrays.asList(sender)));
            }
        }
    }

    private void updateOut(Map<String, List<String>> out, String sender, String[] receivers) {
        if (out.containsKey(sender)) {
            out.get(sender).addAll(Arrays.asList(receivers));
        } else {
            out.put(sender, new ArrayList<String>(Arrays.asList(receivers)));
        }
    }
}