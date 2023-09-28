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
            self.tiempo_transcurrido -= 1
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

cultivo1 = Cultivo("Tomate", 5, 10)
cultivo2 = Cultivo("Maíz", 7, 15)
cultivo3 = Cultivo("Manzana", 10, 20)
cultivo4 = Cultivo("Zanahoria", 6, 12)
cultivo5 = Cultivo("Papa", 8, 18)


while True:
    print("\nMenú de acciones:")
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
