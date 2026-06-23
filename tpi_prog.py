import csv

ARCHIVO_CSV = "paises.csv"


def cargar_paises():
    paises = []

    try:
        with open(ARCHIVO_CSV, encoding="utf-8") as archivo:
            lector = csv.DictReader(archivo)

            for fila in lector:
                paises.append({
                    "nombre": fila["nombre"],
                    "continente": fila["continente"],
                    "poblacion": int(fila["poblacion"]),
                    "superficie": int(fila["superficie"])
                })

    except FileNotFoundError:
        print("Error: No se encontró el archivo paises.csv")

    except Exception as e:
        print("Error al cargar archivo:", e)

    return paises


def guardar_paises(paises):
    try:
        with open(ARCHIVO_CSV, "w", newline="", encoding="utf-8") as archivo:
            campos = ["nombre", "continente", "poblacion", "superficie"]

            escritor = csv.DictWriter(archivo, fieldnames=campos)

            escritor.writeheader()

            for pais in paises:
                escritor.writerow(pais)

    except Exception as e:
        print("Error al guardar:", e)


def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato != "":
            return dato

        print("No puede quedar vacío.")


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Debe ingresar un número.")


def agregar_pais(paises):

    nombre = pedir_texto("Nombre del país: ")
    continente = pedir_texto("Continente: ")

    poblacion = pedir_entero("Población: ")
    superficie = pedir_entero("Superficie: ")

    paises.append({
        "nombre": nombre,
        "continente": continente,
        "poblacion": poblacion,
        "superficie": superficie
    })

    guardar_paises(paises)

    print("País agregado correctamente.")


def actualizar_pais(paises):

    nombre_buscar = input("Ingrese país a actualizar: ")

    for pais in paises:

        if pais["nombre"].lower() == nombre_buscar.lower():

            pais["poblacion"] = pedir_entero("Nueva población: ")
            pais["superficie"] = pedir_entero("Nueva superficie: ")

            guardar_paises(paises)

            print("País actualizado.")
            return

    print("País no encontrado.")


def buscar_pais(paises):

    texto = input("Ingrese nombre a buscar: ")

    encontrados = False

    for pais in paises:

        if texto.lower() in pais["nombre"].lower():
            print(pais)
            encontrados = True

    if not encontrados:
        print("No se encontraron resultados.")


def filtrar_paises(paises):

    continente = input("Continente (Enter para todos): ").strip()

    print("\nRango de población")
    pob_min = input("Mínima (Enter para omitir): ").strip()
    pob_max = input("Máxima (Enter para omitir): ").strip()

    print("\nRango de superficie")
    sup_min = input("Mínima (Enter para omitir): ").strip()
    sup_max = input("Máxima (Enter para omitir): ").strip()

    encontrados = False

    for pais in paises:

        if continente != "":
            if pais["continente"].lower() != continente.lower():
                continue

        if pob_min != "":
            if pais["poblacion"] < int(pob_min):
                continue

        if pob_max != "":
            if pais["poblacion"] > int(pob_max):
                continue

        if sup_min != "":
            if pais["superficie"] < int(sup_min):
                continue

        if sup_max != "":
            if pais["superficie"] > int(sup_max):
                continue

        print(pais)
        encontrados = True

    if not encontrados:
        print("No se encontraron países.")


def ordenar_paises(paises):

    print("\n1- Nombre")
    print("2- Continente")
    print("3- Población")
    print("4- Superficie")

    opcion = input("Elegí criterio: ")

    if opcion == "1":
        criterio = "nombre"
    elif opcion == "2":
        criterio = "continente"
    elif opcion == "3":
        criterio = "poblacion"
    elif opcion == "4":
        criterio = "superficie"
    else:
        print("Opción inválida.")
        return

    orden = input("A = Ascendente | D = Descendente: ").upper()

    reverse = orden == "D"

    ordenados = sorted(
        paises,
        key=lambda p: p[criterio],
        reverse=reverse
    )

    for pais in ordenados:
        print(pais)


def mostrar_estadisticas(paises):

    if len(paises) == 0:
        print("No hay datos.")
        return

    mayor = max(paises, key=lambda p: p["poblacion"])
    menor = min(paises, key=lambda p: p["poblacion"])

    print("\nMayor población:")
    print(mayor["nombre"], "-", mayor["poblacion"])

    print("\nMenor población:")
    print(menor["nombre"], "-", menor["poblacion"])

    promedio_pob = sum(p["poblacion"] for p in paises) / len(paises)
    promedio_sup = sum(p["superficie"] for p in paises) / len(paises)

    print("\nPromedio población:", round(promedio_pob, 2))
    print("Promedio superficie:", round(promedio_sup, 2))

    continentes = {}

    for pais in paises:

        cont = pais["continente"]

        if cont in continentes:
            continentes[cont] += 1
        else:
            continentes[cont] = 1

    print("\nCantidad por continente:")

    for continente, cantidad in continentes.items():
        print(continente, ":", cantidad)


def mostrar_todos(paises):

    for pais in paises:
        print(pais)


def menu():

    paises = cargar_paises()

    while True:

        print("\n===== MENÚ =====")
        print("1- Agregar país")
        print("2- Actualizar país")
        print("3- Buscar país")
        print("4- Filtrar países")
        print("5- Ordenar países")
        print("6- Mostrar estadísticas")
        print("7- Mostrar todos")
        print("0- Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            agregar_pais(paises)

        elif opcion == "2":
            actualizar_pais(paises)

        elif opcion == "3":
            buscar_pais(paises)

        elif opcion == "4":
            filtrar_paises(paises)

        elif opcion == "5":
            ordenar_paises(paises)

        elif opcion == "6":
            mostrar_estadisticas(paises)

        elif opcion == "7":
            mostrar_todos(paises)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")


menu()