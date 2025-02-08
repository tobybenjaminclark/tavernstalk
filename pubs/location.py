from dataclasses import dataclass

@dataclass
class Location():
    latitude: float
    longitude: float
    name: str
    attr: dict

    def __repr__(self) -> str:
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Location):
            return False
        return (self.latitude, self.longitude) == (other.latitude, other.longitude)

    def __hash__(self):
        # You must return an integer that is stable for the object's lifetime
        return hash((self.latitude, self.longitude))

    def get_weight(self) -> float:
        return 5