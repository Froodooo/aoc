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
        // for (String module : modules.keySet()) {
        // System.out.println(module);
        // }
        Queue<Message> queue = new ArrayDeque<Message>();

        int lowPulses = 0;
        int highPulses = 0;

        for (int i = 0; i < 1000; i++) {
            queue.add(new Message(Pulse.LOW, "start", "broadcaster"));

            while (!queue.isEmpty()) {
                // for (Message m : queue) {
                //     System.out.println(m.toString());
                // }
                // System.out.println("\n");

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

        System.out.println("lowPulses: " + lowPulses);
        System.out.println("highPulses: " + highPulses);

        return lowPulses * highPulses;
    }

    public int partB() {
        Map<String, Module> modules = parseInput(input);
        // for (String module : modules.keySet()) {
        // System.out.println(module);
        // }
        Queue<Message> queue = new ArrayDeque<Message>();

        int lowPulses = 0;
        int highPulses = 0;

        boolean rxReceivedLow = false;

        while (!rxReceivedLow) {
            queue.add(new Message(Pulse.LOW, "start", "broadcaster"));

            while (!queue.isEmpty()) {
                // for (Message m : queue) {
                //     System.out.println(m.toString());
                // }
                // System.out.println("\n");

                Message message = queue.poll();
                if (message.getReceiver().equals("rx") && message.getPulse() == Pulse.HIGH) {
                    rxReceivedLow = true;
                }

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

        System.out.println("lowPulses: " + lowPulses);
        System.out.println("highPulses: " + highPulses);

        return lowPulses * highPulses;
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

        // for (String sender : in.keySet()) {
        // System.out.println(sender + " -> " + in.get(sender));
        // }

        // for (String sender : out.keySet()) {
        // System.out.println(sender + " -> " + out.get(sender));
        // }

        for (String name : moduleNames) {
        System.out.println(name);
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

        // for (Module module : modules.values()) {
        // System.out.println(module.toString());
        // }

        // for (String module : modules.keySet()) {
        // System.out.println(module);
        // }

        return modules;
    }

    private void updateModuleNames(Set<String> moduleNames, String sender, String[] receivers) {
        // System.out.println(sender);
        // System.out.println(Arrays.toString(receivers));
        // System.out.println(moduleNames);
        // System.out.println("\n");

        if (moduleNames.contains(sender.replaceAll("[&%]", "")) && !sender.equals("broadcaster")) {
            moduleNames.remove(sender.replaceAll("[&%]", ""));
            moduleNames.add(sender);
        } else if (!moduleNames.contains("%" + sender) && !moduleNames.contains("&" + sender)) {
            moduleNames.add(sender);
        }

        for (String receiver : receivers) {
            if (moduleNames.contains(receiver.replaceAll("[&%]", ""))) {
                // System.out.println("contains");
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