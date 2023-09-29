import random

class Animales:
    def __init__ (self, nombre, salud, felicidad, hambre, produccion):
        self.nombre = nombre 
        self.salud = salud
        self.felicidad = felicidad
        self.hambre = hambre
        self.produccion = produccion

    def alimentar(self):
        self.hambre = 100
        self.salud += 10
        self.felicidad += 10

    def acariciar(self):
        self.felicidad = 100
        self.salud += 10

    def limpiar(self):
        self.salud += 10

    def recolectar(self):
        self.produccion = 100
        self.salud += 10
        self.felicidad += 10

    def mostrar(self):
        print('Nombre:', self.nombre, '   Salud:', self.salud, '   Felicidad:', self.felicidad, '   Hambre:', self.hambre, '   Produccion:', self.produccion)
        

   


class Vacas(Animales):
    def __init__(self, tipo_animal, nombre_animal, edad_animal, peso_animal, color_vaca, raza_vaca):
        super().__init__(tipo_animal, nombre_animal, edad_animal, peso_animal)
        self.color_vaca = color_vaca
        self.raza_vaca = raza_vaca

    def ingresar_datos_vaca(self):
        self.color_vaca = input('Ingrese el color de la vaca: ')
        self.raza_vaca = input('Ingrese la raza de la vaca: ')

    def mostrar_vaca(self):
        print('Color de la vaca:', self.color_vaca, '   Raza de la vaca:', self.raza_vaca)
    

class Gallinas(Animales):
    def __init__(self, tipo_animal, nombre_animal, edad_animal, peso_animal, color_gallina, raza_gallina):
        super().__init__(tipo_animal, nombre_animal, edad_animal, peso_animal)
        self.color_gallina = color_gallina
        self.raza_gallina = raza_gallina

    def ingresar_datos_gallina(self):
        self.color_gallina = input('Ingrese el color de la gallina: ')
        self.raza_gallina = input('Ingrese la raza de la gallina: ')

    def mostrar_gallina(self):
        print('Color de la gallina:', self.color_gallina, '   Raza de la gallina:', self.raza_gallina)
    

class Caballos(Animales):
    def __init__(self, tipo_animal, nombre_animal, edad_animal, peso_animal, color_caballo, raza_caballo):
        super().__init__(tipo_animal, nombre_animal, edad_animal, peso_animal)
        self.color_caballo = color_caballo
        self.raza_caballo = raza_caballo

    def ingresar_datos_caballo(self):
        self.color_caballo = input('Ingrese el color del caballo: ')
        self.raza_caballo = input('Ingrese la raza del caballo: ')

    def mostrar_caballo(self):
        print('Color del caballo:', self.color_caballo, '   Raza del caballo:', self.raza_caballo)


class Ovejas(Animales):
    def __init__(self, tipo_animal, nombre_animal, edad_animal, peso_animal, color_oveja, raza_oveja):
        super().__init__(tipo_animal, nombre_animal, edad_animal, peso_animal)
        self.color_oveja = color_oveja
        self.raza_oveja = raza_oveja

    def ingresar_datos_oveja(self):
        self.color_oveja = input('Ingrese el color de la oveja: ')
        self.raza_oveja = input('Ingrese la raza de la oveja: ')

    def mostrar_oveja(self):
        print('Color de la oveja:', self.color_oveja, '   Raza de la oveja:', self.raza_oveja)
    

while True:
    print('1. Ingresar datos de los animales')
    print('2. Mostrar datos de los animales')
    print('3. Salir')
    opcion = int(input('Ingrese una opcion: '))

    if opcion == 1:
        print('1. Ingresar datos de las vacas')
        print('2. Ingresar datos de las gallinas')
        print('3. Ingresar datos de los caballos')
        print('4. Ingresar datos de las ovejas')
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            vaca1 = Vacas('', '', '', '', '', '')
            vaca1.ingresar_datos()
            vaca1.ingresar_datos_vaca()
        elif opcion == 2:
            gallina1 = Gallinas('', '', '', '', '', '')
            gallina1.ingresar_datos()
            gallina1.ingresar_datos_gallina()
        elif opcion == 3:
            caballo1 = Caballos('', '', '', '', '', '')
            caballo1.ingresar_datos()
            caballo1.ingresar_datos_caballo()
        elif opcion == 4:
            oveja1 = Ovejas('', '', '', '', '', '')
            oveja1.ingresar_datos()
            oveja1.ingresar_datos_oveja()
        else:
            print('Ingrese una opcion valida')
    elif opcion == 2:
        print('1. Mostrar datos de las vacas')
        print('2. Mostrar datos de las gallinas')
        print('3. Mostrar datos de los caballos')
        print('4. Mostrar datos de las ovejas')
        opcion = int(input('Ingrese una opcion: '))

        if opcion == 1:
            vaca1.mostrar()
            vaca1.mostrar_vaca()
        elif opcion == 2:
            gallina1.mostrar()
            gallina1.mostrar_gallina()
        elif opcion == 3:
            caballo1.mostrar()
            caballo1.mostrar_caballo()
        elif opcion == 4:
            oveja1.mostrar()
            oveja1.mostrar_oveja()
        else:
            print('Ingrese una opcion valida')
    elif opcion == 3:
        break
    else:
        print('Ingrese una opcion valida')



