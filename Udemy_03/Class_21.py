"""
Abstract class - Abstract Base Class (abc)
ABCs are used like contracts for definition new classes.
They can to force another classes to create concrete methods.
They may also have concrete methods of their own.
@abstract_methods are methods that no have body.
The rules for abstract classes with abstract methods is they cannot be instantiated directly.
Abstract method must be implemented in subclasses (@abstract_method).
An abstract class in Python has your metaclass be ABCMeta.
It's possible to create @property, @setter, @class_method, @staticmethod and @method like abstract, and for that
use @abstract_method like decorator more internal.
"""
from abc import ABC, abstractmethod


class Log(ABC):
    @abstractmethod
    def _log(self, message):
        ...

    def log_error(self, message):
        return self._log(f'Error: {message}')

    def log_success(self, message):
        return self._log(f'Success: {message}')


class LogPrintMixin(Log):
    def _log(self, message):
        print(f'{message} {self.__class__.__name__}')
        print('Estou retornando o log da classe LogPrintMixin')


log_test = LogPrintMixin()
log_test.log_success('Teste')
