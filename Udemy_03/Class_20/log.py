# Abstraction
# Heritage - Is child

from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'


class Log:
    def _log(self, message):
        raise NotImplemented('Implemente o método log')

    def log_error(self, message):
        return self._log(f'Error: {message}')

    def log_success(self, message):
        return self._log(f'Success: {message}')


class LogFileMixin(Log):
    def _log(self, message):
        formatted_message = f'{message} ({self.__class__.__name__})'
        print('Salvando o log:', formatted_message)
        with open(LOG_FILE, 'a') as file:
            file.write(formatted_message)
            file.write('\n')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} {self.__class__.__name__}')
        print('Estou retornando o log da classe LogPrintMixin')


if __name__ == '__main__':
    log_test = LogPrintMixin()
    log_test.log_error('Qualquer coisa')
    log_test.log_success('Que legal')
    log_file = LogFileMixin()
    log_file.log_error('Another thing')
    log_file.log_success('Right thing')
    print(LOG_FILE)
