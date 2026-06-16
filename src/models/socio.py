from dataclasses import dataclass, field
from models.libro import Libro

@dataclass
class Socio:
    nombre: str
    codigo: int
    libros_en_posesion: list[Libro] = field(default_factory=list)