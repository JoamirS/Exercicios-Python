from log import LogPrintMixin


class Electronic:
    def __init__(self, name):
        self._name = name
        self._power_on = False

    def turn_on(self):
        if not self._power_on:
            self._power_on = True

    def turn_off(self):
        if self._power_on:
            self._power_on = False


class Smartphone(Electronic, LogPrintMixin):
    def turn_on(self):
        super().turn_on()

        if self._power_on:
            message_electronic = f'{self._name} está ligado'
            self.log_success(message_electronic)

    def turn_off(self):
        super().turn_off()

        if not self._power_on:
            message_electronic = f'{self._name} está desligado'
            self.log_success(message_electronic)
