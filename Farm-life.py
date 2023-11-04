
import random
class Cultivo:
    def __init__(self, nombre, tiempo, rendimiento):
        self.nombre = nombre
        self.tiempo_crecimiento = tiempo
        self.rendimiento_maximo = rendimiento
        self.estado = "sin sembrar"
        self.tiempo_transcurrido = 0
        self.cosecha_actual = 0
        self.plagas = 0

    def sembrar(self):
        if self.estado == "sin sembrar":
            self.estado = "en crecimiento"
            self.tiempo_transcurrido = 0
            self.cosecha_actual = 0
            self.plagas = 0
            print(f"Has sembrado {self.nombre}.")
        else:
            print(f"{self.nombre} ya ha sido sembrado.")

    def regar(self):
        if self.estado == "en crecimiento":
            self.tiempo_transcurrido += 1
            self.cosecha_actual += random.randint(1, 5)
            if random.random() < 0.1:
                self.plagas += 1
                print(f"{self.nombre} ha sido afectado por plagas.")
            print(f"{self.nombre} ha sido regado.")
            if self.tiempo_transcurrido >= self.tiempo_crecimiento:
                self.estado = "Listo para cosechar"
                print(f"{self.nombre} está listo para ser cosechado.")
        elif self.estado == "sin sembrar":
            print(f"Primero debes sembrar {self.nombre}.")
        else:
            print(f"{self.nombre} está listo para ser cosechado.")

    def cosechar(self):
        if self.estado == "Listo para cosechar":
            cosecha = min(self.cosecha_actual, self.rendimiento_maximo)
            print(f"Has cosechado {cosecha} unidades de {self.nombre}.")
            self.estado = "sin sembrar"
        elif self.estado == "en crecimiento":
            print(f"{self.nombre} aún no esta listo. Deja que crezca un poco más.")
        elif self.estado == "sin sembrar":
            print(f"Primero debes sembrar y regar {self.nombre} para que crezca.")

    def fertilizante(self):
        if self.estado == "en crecimiento":
            self.tiempo_transcurrido += 1
            print(f"Has aplicado fertilizante a {self.nombre}. Su crecimiento se ha acelerado.")
        elif self.estado == "sin sembrar":
            print(f"No puedes aplicar fertilizante a {self.nombre} si no ha sido sembrado.")
        else:
            print(f"{self.nombre} ya esta listo y no necesita más fertilizante.")

    def tratar_plagas(self):
        if self.estado == "en crecimiento" and self.plagas > 0:
            self.plagas = 0
            print(f"Has tratado las plagas en {self.nombre}.")
        elif self.estado == "en crecimiento" and self.plagas == 0:
            print(f"{self.nombre} no tiene plagas en este momento.")
        elif self.estado == "sin sembrar":
            print(f"No puedes tratar plagas en {self.nombre} si no ha sido sembrado.")
        else:
            print(f"{self.nombre} ya esta listo y no necesita tratamiento de plagas.")

cultivo1 = Cultivo("Limon", 3, 11)
cultivo2 = Cultivo("Aguacate", 4, 18)
cultivo3 = Cultivo("Fresa", 10, 20)
cultivo4 = Cultivo("Lechuga", 5, 16)
cultivo5 = Cultivo("Rabano", 7, 15)


class Animal:
    def __init__(self, nombre, salud, hambre, felicidad, produccion):
        self.nombre = nombre
        self.salud = salud
        self.hambre = hambre
        self.felicidad = felicidad
        self.produccion = produccion
        self.enfermo = False

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
        self.enfermo = False

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


        if self.salud < 50 and random.random() < 0.3:
            self.enfermo = True
            self.produccion *= 0.5
            self.felicidad *= 0.7


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
            jugador.aumentar_experiencia(50 * len(animales))
        elif opcion == '3':
            acariciar_animales(animales)
            jugador.aumentar_experiencia(50 * len(animales))
        elif opcion == '4':
            limpiar_animales(animales)
            jugador.aumentar_experiencia(50 * len(animales))
        elif opcion == '5':
            recursos_obtenidos = recolectar_recursos(animales)
            print(f"\nHas recolectado {recursos_obtenidos} recursos de los animales.")
            jugador.aumentar_experiencia(50 * len(animales))
        elif opcion == '6':
            jugador.mostrar_experiencia()
        elif opcion == '7':
            reiniciar_estado(animales)
        elif opcion == '8':
            break
        else:
            print("Opción inválida. Por favor, elige una opción válida.")

        for animal in animales:
            animal.actualizar()
while True:
    Main_menu=input("que desea Gestionar?\nA.Cultivos\nB.Animales")
    if Main_menu.upper() == "A":
        while True:
            print("\nMenú:")
            print("1. Sembrar cultivo")
            print("2. Regar cultivo")
            print("3. Cosechar cultivo")
            print("4. Aplicar fertilizante")
            print("5. Tratar plagas")
            print("6. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                cultivo = int(input("Selecciona un cultivo para sembrar (1-5): "))
                if cultivo == 1:
                    cultivo1.sembrar()
                elif cultivo == 2:
                    cultivo2.sembrar()
                elif cultivo == 3:
                    cultivo3.sembrar()
                elif cultivo == 4:
                    cultivo4.sembrar()
                elif cultivo == 5:
                    cultivo5.sembrar()
                else:
                    print("Opción no válida.")

            elif opcion == "2":
                cultivo = int(input("Selecciona un cultivo para regar (1-5): "))
                if cultivo == 1:
                    cultivo1.regar()
                elif cultivo == 2:
                    cultivo2.regar()
                elif cultivo == 3:
                    cultivo3.regar()
                elif cultivo == 4:
                    cultivo4.regar()
                elif cultivo == 5:
                    cultivo5.regar()
                else:
                    print("Opción no válida.")

            elif opcion == "3":
                cultivo = int(input("Selecciona un cultivo para cosechar (1-5): "))
                if cultivo == 1:
                    cultivo1.cosechar()
                elif cultivo == 2:
                    cultivo2.cosechar()
                elif cultivo == 3:
                    cultivo3.cosechar()
                elif cultivo == 4:
                    cultivo4.cosechar()
                elif cultivo == 5:
                    cultivo5.cosechar()
                else:
                    print("Opción no válida.")

            elif opcion == "4":
                cultivo = int(input("Selecciona un cultivo para aplicar fertilizante (1-5): "))
                if cultivo == 1:
                    cultivo1.fertilizante()
                elif cultivo == 2:
                    cultivo2.fertilizante()
                elif cultivo == 3:
                    cultivo3.fertilizante()
                elif cultivo == 4:
                    cultivo4.fertilizante()
                elif cultivo == 5:
                    cultivo5.fertilizante()
                else:
                    print("Opción no válida.")

            elif opcion == "5":
                cultivo = int(input("Selecciona un cultivo para tratar plagas (1-5): "))
                if cultivo == 1:
                    cultivo1
            elif opcion == "6":
                break
    if Main_menu.upper() == "B":
        if __name__ == "__main__":
            main()

