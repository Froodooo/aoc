package day20;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import day20.Message.Pulse;

public class ConjunctionModule implements Module {

    String name;
    String[] out;
    String[] in;
    Map<String, Pulse> received;

    public ConjunctionModule(String name, String[] out, String[] in) {
        this.name = name;
        this.out = out;
        this.in = Arrays.asList(in).stream().map(i -> i.replaceAll("[&%]", "")).toArray(String[]::new);

        received = new HashMap<String, Pulse>();
        for (String i : this.in) {
            received.put(i, Pulse.LOW);
        }
    }

    @Override
    public List<Message> handleMessage(Message message) {
        received.put(message.getSender(), message.getPulse());

        List<Message> messages = new ArrayList<>();

        for (String out : this.out) {
            Pulse pulse = received.values().stream().allMatch(p -> p == Pulse.HIGH) ? Pulse.LOW : Pulse.HIGH;
            messages.add(new Message(pulse, name, out));
        }

        return messages;
    }

    public String toString() {
        return "ConjunctionModule [name=" + name + ", out=" + Arrays.toString(out) + ", in=" + Arrays.toString(in)
                + "]";
    }

    @Override
    public String[] getOut() {
        return out;
    }
}
