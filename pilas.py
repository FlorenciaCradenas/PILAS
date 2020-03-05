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
msj: str
msj_inverse: str = ''

msj = input('Dame un mensaje: ')
for i in msj:
    stack.push(i)

while not stack.empty():
    msj_inverse = msj_inverse + stack.pop()

print('El mensaje inverso es: ', msj_inverse)