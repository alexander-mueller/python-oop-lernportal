public interface INotificationsService {
    bool SendeNachricht(string empfaenger, string text);
}

public class EmailNotificationService : INotificationsService {
    public bool SendeNachricht(string empfaenger, string text) => true;
}