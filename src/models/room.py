class Room:
    def __init__(self, name: str, capacity: int, equipment: list[str]):
        self._name = name
        self._capacity = capacity
        self._equipment = equipment

    @property
    def name(self) -> str:
        return self._name

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def equipment(self) -> list[str]:
        return self._equipment

    def has_equipment(self, item: str) -> bool:
        return item.lower() in (e.lower() for e in self._equipment)

    def __str__(self):
        return f"Room(name={self._name}, capacity={self._capacity}, equipement={self._equipment})"
