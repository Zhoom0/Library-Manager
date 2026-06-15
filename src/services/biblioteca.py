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

    