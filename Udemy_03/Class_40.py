from dataclasses import dataclass, asdict, field


@dataclass
class Person:
    name: str = field(default='Missing', repr=False)
    last_name: str = 'Not Send'
    age: int = 0

    def __post_init__(self):
        print(f'{self.name}')

    @property
    def full_name(self):
        return f'{self.name} {self.last_name}'


if __name__ == '__main__':
    person_01 = Person('Otavio', 'Luiz', 30)
    full_name = person_01.full_name
    print(person_01)
    print(full_name)
    print(asdict(person_01))
