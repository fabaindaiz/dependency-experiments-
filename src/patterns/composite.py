from typing import TypeVar

T = TypeVar('T')

class Composite(T):
    def __init__(self) -> None:
        self.children: list[T] = []

    def add(self, component: T) -> None:
        self.children.append(component)

    def remove(self, component: T) -> None:
        self.children.remove(component)

    def getChildren(self) -> list[T]:
        return self