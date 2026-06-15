from models.libro import Libro
from models.socio import Socio

class Biblioteca:
    def __init__(self):
        self.libros: list[Libro] = []
        self.socios: list[Socio] = []

    def agregar_libro(self, libro_para_agregar: Libro) -> None:
        if libro_para_agregar:
            self.libros.append(libro_para_agregar)
            print("Libro agregado exitosamente.")
            return None
        else:
            print("No se pudo agregar el libro, por favor ingrese un libro valido.")

    def agregar_socio(self, socio_para_agregar: Socio) -> None:
        if socio_para_agregar:
            self.socios.append(socio_para_agregar)
            print("Socio agregado exitosamente.")
            return None
        else:
            print("No se pudo agregar el socio, por favor ingrese un socio valido.")

    def prestar_libro(self, libro_para_prestar: Libro, socio_para_prestar: Socio) -> None:
        if libro_para_prestar is None:
            print("Por favor seleccione un libro valido.")
            return None
        if not libro_para_prestar.disponible:
            print("ERROR: Este libro ya se encuentra prestado.")
            return None
        
        if socio_para_prestar is None:
            print("Por favor seleccione un socio valido.")
            return None
        if libro_para_prestar in socio_para_prestar.libros_en_posesion:
            print("ERROR: Este socio ya posee ese libro.")
            return None