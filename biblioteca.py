titulos = []
autores = []
anios = [] 
cantidad_disponible = []

def dar_posicion_del_titulo(titulo):
    for i in range(len(titulos)):
        if titulos[i] == titulo:
            return i
            
def buscar_libro_por_titulo(titulo_a_buscar):
    esta = False
    for titulo in titulos:
        if titulo == titulo_a_buscar:
            esta = True          
    return esta   
     
def agregar_libro():
    titulo = input("Ingresar el título: ")
    autor = input("Ingresar el autor: ")
    anio = int(input("Ingresar el año: "))
    cantidad = int(input("Ingresar cantidad: "))

    if buscar_libro_por_titulo(titulo) == False:
        titulos.append(titulo)
        autores.append(autor)
        anios.append(anio)
        cantidad_disponible.append(cantidad)
    else:
        i = dar_posicion_del_titulo
        cantidad_disponible[i] += cantidad
    print("Libro agregado correctamente")
    
def mostrar_libros():
    if titulos == []:
        print("No hay libros cargados")
    else:
        print("Muestro libros ordenados por títulos, autores y año de publicación")
        print(f"Libros: {titulos}")
        print(f"Autores: {autores}")
        print(f"Año: {anios}")

def prestar_libro():
    titulo = input("Ingresar el título del libro a prestar: ")
    if buscar_libro_por_titulo(titulo) == False:
        print("No se puede prestar un libro que nunca estuvo cargado")
    else:
        i = dar_posicion_del_titulo(titulo)
        if cantidad_disponible[i] == 0:
            print("No se puede prestar un libro si no hay ejemplares disponibles")
        else:
            cantidad_disponible[i] -= 1
            print("Libro prestado")

def devolver_libro():
    titulo = input("Ingresar el título: ")
    if buscar_libro_por_titulo(titulo) == False:
        print("No se puede devolver un libro que nunca estuvo cargado")
    else:
        i = dar_posicion_del_titulo(titulo)
        cantidad_disponible[i] += 1
        print("Libro devuelto")

def mostrar_libros_sin_stock():
    libros_sin_stock = []
    autores_sin_stock = []
    for i in range(len(cantidad_disponible)):
        if cantidad_disponible[i] == 0:
            libros_sin_stock.append(titulos[i])
            autores_sin_stock.append(autores[i])
    print(f"Libros: {libros_sin_stock}") 
    print(f"Autores: {autores_sin_stock}")

def inicio_biblioteca():
    print("1. Agregar libro")
    print("2. Mostrar todos los libros")
    print("3. Buscar libro por título")
    print("4. Prestar libro")
    print("5. Devolver libro")
    print("6. Mostrar libros sin stock")
    print("7. Salir")
    
    opcion = int(input("Elige una de las siguiente opciones: "))
    return opcion

def main():

    opcion = inicio_biblioteca()
   
    while opcion != 7:
        match opcion:
            case 1: 
                agregar_libro()
            case 2:
                mostrar_libros()
            case 3:
                titulo = input("Ingresa el titulo a buscar: ")
                esta =buscar_libro_por_titulo(titulo)
                if esta == True:
                    i = dar_posicion_del_titulo(titulo)
                    print(f"Cantidad disponible: {cantidad_disponible[i]}")
                    print("El libro está en la biblioteca")
                else:
                    print("El libro no está en la biblioteca")
            case 4: 
                prestar_libro()
            case 5:
                devolver_libro() 
            case 6:
                print(mostrar_libros_sin_stock())
            case _:
                print("Por favor elige una opción válida(del 1 al 7)")
        opcion = inicio_biblioteca()
    print("Saliste de la biblioteca")

main()