from dataclasses import dataclass
from libro import Libro

@dataclass
class Socio:
    nombre: str
    id: int
    libros_en_posesion: list[Libro]