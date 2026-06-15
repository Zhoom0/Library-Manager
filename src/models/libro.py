from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    id: int
    disponible: bool = True