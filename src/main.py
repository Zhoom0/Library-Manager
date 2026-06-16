from models.libro import Libro
from models.socio import Socio
from services.biblioteca import Biblioteca

if __name__ == "__main__":
    local1 = Biblioteca()

    libro1 = Libro("Tres días", "Cristobal", 9876557)
    libro2 = Libro("Amanecer", "Dieg", 172371)
    libro3 = Libro("Anochecer", "Dieguito", 3172312)

    local1.agregar_libro(libro1)
    local1.agregar_libro(libro2)
    local1.agregar_libro(libro3)

    socio1 = Socio("Papaleta", 123123)
    socio2 = Socio("Matías", 543543)

    local1.agregar_socio(socio1)
    local1.agregar_socio(socio2)

    local1.prestar_libro(libro1, socio1)

    print(local1.listar_libros_disponibles())

    local1.libros_socio(socio1)

    local1.devolver_libro(libro1, socio1)