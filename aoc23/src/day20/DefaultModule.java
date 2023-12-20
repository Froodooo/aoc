package day20;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DefaultModule implements Module {

    String name;
    String[] out;

    public DefaultModule(String name, String[] out) {
        this.name = name;
        this.out = out;
    }

    @Override
    public List<Message> handleMessage(Message message) {
        List<Message> messages = new ArrayList<>();
        
        for (String out : this.out) {
            messages.add(new Message(message.getPulse(), name, out));
        }

        return messages;
    }
    
    public String toString() {
        return "DefaultModule [name=" + name + ", out=" + Arrays.toString(out) + "]";
    }

    @Override
    public String[] getOut() {
        return out;
    }
}
