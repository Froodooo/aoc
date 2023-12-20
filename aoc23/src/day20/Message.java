package day20;

public class Message {
    public enum Pulse {
        HIGH, LOW
    }

    private Pulse pulse;
    private String sender;
    private String receiver;

    public Message(Pulse pulse, String sender, String receiver) {
        this.pulse = pulse;
        this.sender = sender;
        this.receiver = receiver;
    }

    public Pulse getPulse() {
        return pulse;
    }

    public String getSender() {
        return sender;
    }

    public String getReceiver() {
        return receiver;
    }

    public String toString() {
        return "Message [pulse=" + pulse + ", sender=" + sender + ", receiver=" + receiver + "]";
    }
}
