from models.libro import Libro
from models.socio import Socio

class Biblioteca:
    def __init__(self):
        self.libros: list[Libro] = []
        self.socios: list[Socio] = []
        
    def agregar_libro(self, libro_para_agregar: Libro) -> None:
        if not libro_para_agregar:
            raise ValueError("ERROR: Ingrese un libro valido.")
        if libro_para_agregar in self.libros:
            raise ValueError("ERROR: Este libro ya se encuentra en la biblioteca.")
        
        self.libros.append(libro_para_agregar)
        print("Libro agregado exitosamente.")
        return None

    def agregar_socio(self, socio_para_agregar: Socio) -> None:
        if not socio_para_agregar:
            raise ValueError("ERROR: Ingrese un socio valido.")
        if socio_para_agregar in self.socios:
            raise ValueError("ERROR: Este socio ya está registrado en la biblioteca.")
        self.socios.append(socio_para_agregar)
        print("Socio registrado exitosamente.")
        return None

    def prestar_libro(self, libro_para_prestar: Libro, socio_para_prestar: Socio) -> None:
        if libro_para_prestar is None:
            raise ValueError("ERROR: Por favor ingrese un libro valido")
        if socio_para_prestar is None:
            raise ValueError("ERROR: Por favor seleccione un socio valido.")
        if libro_para_prestar in socio_para_prestar.libros_en_posesion:
            raise ValueError("ERROR: Este socio ya posee ese libro.")
        if len(socio_para_prestar.libros_en_posesion) >= 3:
            raise ValueError("ERROR: Un socio no puede tener mas de 3 libros prestados al mismo tiempo")
        if not libro_para_prestar.disponible:
            raise ValueError("ERROR: Este libro ya se encuentra prestado.")
        
        socio_para_prestar.libros_en_posesion.append(libro_para_prestar)
        libro_para_prestar.disponible = False
        print(f"Libro {libro_para_prestar.titulo} prestado exitosamente al socio {socio_para_prestar.nombre}.")
        return None
    
    def devolver_libro(self, libro_para_devolver: Libro, socio_que_devuelve: Socio) -> None:
        if libro_para_devolver is None:
            raise ValueError("ERROR: Por favor ingrese un libro valido")
        if socio_que_devuelve is None:
            raise ValueError("ERROR: Por favor seleccione un socio valido.")
        if libro_para_devolver not in socio_que_devuelve.libros_en_posesion:
            raise ValueError("ERROR: Este socio no tiene este libro.")
        if libro_para_devolver.disponible:
            raise ValueError("ERROR: Este socio no tiene este libro. El libro se encuentra disponible")
        socio_que_devuelve.libros_en_posesion.remove(libro_para_devolver)
        libro_para_devolver.disponible = True
        print(f"Libro {libro_para_devolver.titulo} devuelto exitosamente por socio {socio_que_devuelve.nombre}.")
        return None
    
    def listar_libros_disponibles(self) -> list[Libro] | None:
        return [libro for libro in self.libros if libro.disponible]

    def libros_socio(self, socio_para_revisar: Socio) -> None:
        if socio_para_revisar is None:
            raise ValueError("ERROR: Ingrese un socio valido.")
        if socio_para_revisar.libros_en_posesion == []:
            raise ValueError("ERROR: Este socio no tiene ningún libro en posesion.")
        for libro in socio_para_revisar.libros_en_posesion:
            print(f"{libro.titulo}: Escrito por {libro.autor}.")
        return None
    