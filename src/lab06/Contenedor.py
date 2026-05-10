from typing import TypeVar, Generic, Callable, Optional
from typing import Protocol

class Displayable(Protocol):
    def display(self) -> str:
        ...


class Scorable(Protocol):
    def score(self) -> float:
        ...

T = TypeVar("T")
R = TypeVar("R")
D = TypeVar("D", bound=Displayable)
S = TypeVar("S", bound=Scorable)

class TypedCollection(Generic[T]):

    def __init__(self) -> None:
        self._items: list[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        if item in self._items:
            self._items.remove(item)
        else:
            raise ValueError("El elemento no esta en la coleccion")

    def get_all(self) -> list[T]:
        return list(self._items)

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> list[T]:
        resultado = []
        for item in self._items:
            if predicate(item):
                resultado.append(item)
        return resultado

    def map(self, transform: Callable[[T], R]) -> list[R]:
        resultado = []
        for item in self._items:
            resultado.append(transform(item))
        return resultado

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __str__(self) -> str:
        if len(self._items) == 0:
            return "TypedCollection: vacia"
        else:
            texto = "TypedCollection (" + str(len(self._items)) + " elementos):" + chr(10)
            for i in range(len(self._items)):
                texto = texto + "  [" + str(i) + "] " + str(self._items[i]) + chr(10)
            return texto