import random


class Animal:
    def __init__(self, nombre, salud, hambre, felicidad, produccion):
        self.nombre = nombre
        self.salud = salud
        self.hambre = hambre
        self.felicidad = felicidad
        self.produccion = produccion
        self.enfermo = False  # Nuevo atributo para indicar si el animal está enfermo

    def reset_estado(self):
        self.salud = 0
        self.hambre = 100
        self.felicidad = 0
        self.produccion = 0
        self.enfermo = False

    def alimentar(self):
        self.hambre -= random.randint(5, 15)
        self.salud += random.randint(1, 5)
        self.felicidad += random.randint(1, 5)
        self.hambre = max(0, self.hambre)
        self.enfermo = False  # El animal se cura cuando se alimenta

    def acariciar(self):
        self.felicidad += random.randint(5, 10)
        self.produccion += random.randint(1, 5)

    def limpiar(self):
        self.felicidad += random.randint(1, 5)

    def actualizar(self):
        self.hambre += random.randint(1, 10)
        self.salud -= random.randint(1, 5)
        self.felicidad -= random.randint(1, 5)
        self.produccion -= random.randint(1, 3)
        self.produccion = max(0, self.produccion)
        self.hambre = max(0, self.hambre)

        # El animal tiene una probabilidad de enfermarse si no se cuida adecuadamente
        if self.salud < 50 and random.random() < 0.3:
            self.enfermo = True
            self.produccion *= 0.5  # Disminuir la producción si está enfermo
            self.felicidad *= 0.7  # Disminuir la felicidad si está enfermo

        # Restringir los valores dentro del rango apropiado
        self.salud = max(0, self.salud)
        self.felicidad = max(0, self.felicidad)


class Jugador:
    def __init__(self):
        self.experiencia = 0

    def aumentar_experiencia(self, cantidad):
        self.experiencia += cantidad

    def mostrar_experiencia(self):
        print(f"Experiencia actual: {self.experiencia}")


class Perro(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 100, 0, 70, 0)


class Caballo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 90, 0, 70, 0)


class Gallina(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 70, 0, 70, 0)

    def poner_huevos(self):
        return random.randint(3, 5)


class Pato(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 80, 0, 70, 0)

    def poner_huevos(self):
        return random.randint(2, 4)


class Vaca(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 100, 0, 50, 0)

    def producir_leche(self):
        return random.randint(5, 10)


class Cerdo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 90, 0, 60, 0)

    def producir_carne(self):
        return random.randint(5, 8)


class Oveja(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 80, 0, 60, 0)

    def producir_lana(self):
        return random.randint(1, 3)


class Conejo(Animal):
    def __init__(self, nombre):
        super().__init__(nombre, 70, 0, 50, 0)


def mostrar_menu():
    print("\n--- Granja de Animales ---")
    print("1. Ver estado de los animales")
    print("2. Alimentar animales")
    print("3. Acariciar animales")
    print("4. Limpiar animales")
    print("5. Recolectar recursos")
    print("6. Mostrar experiencia (XP)")
    print("7. Reiniciar estado de los animales")
    print("8. Salir")


def mostrar_avance(animal, antes):
    print(f"\nAntes de la interacción con {animal.nombre}:")
    print(
        f"Salud: {antes['salud']}, Hambre: {antes['hambre']}, Felicidad: {antes['felicidad']}, Producción: {antes['produccion']}")
    print(f"Después de la interacción con {animal.nombre}:")
    print(
        f"Salud: {animal.salud}, Hambre: {animal.hambre}, Felicidad: {animal.felicidad}, Producción: {animal.produccion}")


def recolectar_recursos(animales):
    recursos_totales = 0
    for animal in animales:
        if isinstance(animal, Gallina):
            huevos = animal.poner_huevos()
            recursos_totales += huevos
            animal.produccion -= huevos
        elif isinstance(animal, Pato):
            huevos = animal.poner_huevos()
            recursos_totales += huevos
            animal.produccion -= huevos
        elif isinstance(animal, Vaca):
            leche = animal.producir_leche()
            recursos_totales += leche
            animal.produccion -= leche
        elif isinstance(animal, Cerdo):
            carne = animal.producir_carne()
            recursos_totales += carne
            animal.produccion -= carne
        elif isinstance(animal, Oveja):
            lana = animal.producir_lana()
            recursos_totales += lana
            animal.produccion -= lana
    return recursos_totales


def alimentar_animales(animales):
    print("\n--- Alimentar animales ---")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal.nombre}")
    seleccion = input("Selecciona los animales que deseas alimentar (separados por comas): ")
    indices = [int(idx) - 1 for idx in seleccion.split(",")]
    for idx in indices:
        if 0 <= idx < len(animales):
            animal = animales[idx]
            antes = {'salud': animal.salud, 'hambre': animal.hambre, 'felicidad': animal.felicidad,
                     'produccion': animal.produccion}
            animal.alimentar()
            mostrar_avance(animal, antes)


def acariciar_animales(animales):
    print("\n--- Acariciar animales ---")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal.nombre}")
    seleccion = input("Selecciona los animales que deseas acariciar (separados por comas): ")
    indices = [int(idx) - 1 for idx in seleccion.split(",")]
    for idx in indices:
        if 0 <= idx < len(animales):
            animal = animales[idx]
            antes = {'salud': animal.salud, 'hambre': animal.hambre, 'felicidad': animal.felicidad,
                     'produccion': animal.produccion}
            animal.acariciar()
            mostrar_avance(animal, antes)


def limpiar_animales(animales):
    print("\n--- Limpiar animales ---")
    for i, animal in enumerate(animales, 1):
        print(f"{i}. {animal.nombre}")
    seleccion = input("Selecciona los animales que deseas limpiar (separados por comas): ")
    indices = [int(idx) - 1 for idx in seleccion.split(",")]
    for idx in indices:
        if 0 <= idx < len(animales):
            animal = animales[idx]
            antes = {'salud': animal.salud, 'hambre': animal.hambre, 'felicidad': animal.felicidad,
                     'produccion': animal.produccion}
            animal.limpiar()
            mostrar_avance(animal, antes)


def reiniciar_estado(animales):
    for animal in animales:
        animal.reset_estado()
    print("El estado de los animales ha sido reiniciado.")


def main():
    animales = []
    animales.append(Perro("Perro"))
    animales.append(Caballo("Caballo"))
    animales.append(Gallina("Gallina"))
    animales.append(Pato("Pato"))
    animales.append(Vaca("Vaca"))
    animales.append(Cerdo("Cerdo"))
    animales.append(Oveja("Oveja"))
    animales.append(Conejo("Conejo"))

    jugador = Jugador()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print("\n--- Estado de los animales ---")
            for i, animal in enumerate(animales, 1):
                estado = "Enfermo" if animal.enfermo else "Saludable"
                print(
                    f"{i}. {animal.nombre} - Salud: {animal.salud}, Hambre: {animal.hambre}, Felicidad: {animal.felicidad}, Producción: {animal.produccion}, Estado: {estado}")
        elif opcion == '2':
            alimentar_animales(animales)
            jugador.aumentar_experiencia(50 * len(animales))  # Aumentar experiencia por cada animal alimentado
        elif opcion == '3':
            acariciar_animales(animales)
            jugador.aumentar_experiencia(50 * len(animales))  # Aumentar experiencia por cada animal acariciado
        elif opcion == '4':
            limpiar_animales(animales)
            jugador.aumentar_experiencia(50 * len(animales))  # Aumentar experiencia por cada animal limpiado
        elif opcion == '5':
            recursos_obtenidos = recolectar_recursos(animales)
            print(f"\nHas recolectado {recursos_obtenidos} recursos de los animales.")
            jugador.aumentar_experiencia(50 * len(animales))  # Aumentar experiencia por recolectar recursos
        elif opcion == '6':
            jugador.mostrar_experiencia()
        elif opcion == '7':
            reiniciar_estado(animales)
        elif opcion == '8':
            print("¡Gracias por jugar! Saliendo del juego.")
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

        for animal in animales:
            animal.actualizar()


if __name__ == "__main__":
    main()


