from typing import TypeVar, Generic, List

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        # Create an empty list with items of type T
        self.items: List[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def empty(self) -> bool:
        return not self.items
    def print_stack(self):
        print(self.items)

stack: Stack = Stack()
stack.push('HOLA')
stack.push('AMIGOS')
stack.push('DE TSC')
stack.pop()
stack.print_stack()