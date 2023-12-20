package day20;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import day20.Message.Pulse;

public class FlipFlopModule implements Module {

    String name;
    String[] out;
    int state;

    public FlipFlopModule(String name, String[] out) {
        this.name = name;
        this.out = out;
        this.state = 0;
    }

    @Override
    public List<Message> handleMessage(Message message) {
        List<Message> messages = new ArrayList<>();

        switch (message.getPulse()) {
            case LOW:
                for (String out : this.out) {
                    Pulse pulse = state == 0 ? Pulse.HIGH : Pulse.LOW;
                    messages.add(new Message(pulse, name, out));
                }
                state = state == 0 ? 1 : 0;
                break;
            default:
                break;
        }

        return messages;
    }

    public String toString() {
        return "FlipFlopModule [name=" + name + ", out=" + Arrays.toString(out) + "]";
    }

    @Override
    public String[] getOut() {
        return out;
    }
}
