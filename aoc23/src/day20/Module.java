package day20;

import java.util.List;

public interface Module {
    List<Message> handleMessage(Message message);
    String[] getOut();
}
