from dataclasses import dataclass


@dataclass(frozen=True)
class Entity:

    type: str
    data: dict[str, str]