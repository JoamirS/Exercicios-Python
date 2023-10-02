"""
Polymorphism in POO is a principle that allows derivative class of the same superclass has igual methods (with the same
sign) but with different behaviors.
Sign of Method = Same and amount parameters (return is not part of sign)
SO, 'L', ID
Substitution principle of liskov
Super class objects must be replaceable for objects in subclass without breaking the application.
method overloading (overload) = Do not supported
method override (override) = Supported
"""
from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message):
        self.message = message

    @abstractmethod
    def send(self) -> bool:
        pass


class NotificationEmail(Notification):
    def send(self):
        print('E-mail: Enviando - ', self.message)


class NotificationSMS(Notification):
    def send(self):
        print('SMS: Enviando - ', self.message)


def notify(notification_input: Notification):
    notification_sent = notification_input.send()

    if notification_sent:
        print('Notificação enviada')
    else:
        print('Notificação não enviada')


# test_notification = NotificationSMS('Testando notificação')
# test_notification.send()

notification_email = NotificationEmail('Testando Email')
notify(notification_email)
