from typing import TypeVar,Generic

T = TypeVar('T',bound='person')

class person(Generic[T]):
    def __init__(self,name: str,age: int):
        self.name=name
        self.age=age

    def __repr__(self) -> str:
        return f'{self.name = }&{self.age = }'

    def __lt__(self,other: T) -> bool: # 小于号
        print('Use __lt__')
        return self.age < other.age

    def __gt__(self,other: T) -> bool: # 大于号
        print('Use __gt__')
        return self.age > other.age

    def __eq__(self,other: object) -> bool: # 双等号
        print('Use __eq__')
        if isinstance(other,person):
            return self.age == other.age
        return False

Bob: person = person('Bob', 20)
Tom: person = person('Tom', 25)

print(Bob < Tom)
print(Bob > Tom)
print(Bob == Tom)