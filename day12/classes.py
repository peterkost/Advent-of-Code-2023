from dataclasses import dataclass
from typing import List


@dataclass
class Line:
    springs: List[str]
    checksum: List[int]

    def __str__(self) -> str:
        return f"{self.springs} {','.join(map(str, self.checksum))}"

@dataclass
class State:
    springI: int
    csI: int
    dmgLen: int

    def __str__(self) -> str:
        return f"State: spring index={self.springI}, checksum index={self.csI}, current damage group length={self.dmgLen}"

    def __hash__(self):
        return hash((self.springI, self.csI, self.dmgLen))
