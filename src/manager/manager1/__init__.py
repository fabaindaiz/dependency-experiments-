from abc import ABC, abstractmethod

class Manager1(ABC):
    @abstractmethod
    def do_work(self):
        pass