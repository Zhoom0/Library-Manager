from dataclasses import dataclass

@dataclass
class Libro:
    titulo: str
    autor: str
    codigo: int
    disponible: bool = True