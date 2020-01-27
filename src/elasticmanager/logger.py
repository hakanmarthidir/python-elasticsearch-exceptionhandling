from abc import abstractmethod, ABC


class Logger(ABC):
    @abstractmethod
    def write(self, obj):
        pass
