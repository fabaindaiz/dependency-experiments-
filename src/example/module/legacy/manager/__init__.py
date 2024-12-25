from abc import ABC, abstractmethod
from dependency.core import Component, component

class Manager(ABC):
    @abstractmethod
    def work(self) -> None:
        pass

@component(
    interface=Manager
)
class ManagerComponent(Component):
    pass