from models.libro import Libro
from models.socio import Socio

class Biblioteca:
    def __init__(self):
        self.libros: list[Libro] = []
        self.socios: list[Socio] = []

    def agregar_libro(self, libro_para_agregar: Libro) -> None:
        if not libro_para_agregar:
            raise ValueError("Error: Ingrese un libro valido.")
        if libro_para_agregar in self.libros:
            raise ValueError("ERROR: Este libro ya se encuentra en la biblioteca.")
        self.libros.append(libro_para_agregar)
        print("Libro agregado exitosamente.")
        return None

    def agregar_socio(self, socio_para_agregar: Socio) -> None:
        if not socio_para_agregar:
            raise ValueError("Error: Ingrese un socio valido.")
        if socio_para_agregar in self.libros:
            raise ValueError("ERROR: Este socio ya está registrado en la biblioteca.")
        self.libros.append(socio_para_agregar)
        print("Socio registrado exitosamente.")
        return None

    def prestar_libro(self, libro_para_prestar: Libro, socio_para_prestar: Socio) -> None:
        if libro_para_prestar is None:
            raise ValueError("Por favor ingrese un libro valido")
        if not libro_para_prestar.disponible:
            raise ValueError("ERROR: Este libro ya se encuentra prestado.")
        
        if socio_para_prestar is None:
            raise ValueError("Por favor seleccione un socio valido.")
        if libro_para_prestar in socio_para_prestar.libros_en_posesion:
            raise ValueError("ERROR: Este socio ya posee ese libro.")