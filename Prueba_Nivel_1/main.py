class Vehiculo:
    def mostrar_menu():
        vehiculos = [Coche(), Camion(), Motocicleta(), Bicicleta()]
        while True:
            print("\nMenú de Vehículos:")
            print("1. Coche")
            print("2. Camión")
            print("3. Motocicleta")
            print("4. Bicicleta")
            print("5. Salir")
            seleccion = int(input("Seleccione el número del vehículo que desea: "))
            if 1 <= seleccion <= 4:
                print(f"Ha seleccionado: {vehiculos[seleccion - 1]}")
            elif seleccion == 5:
                print("Saliendo del menú...")
                break
            else:
                print("Selección no válida")

    def __init__(self, ruedas):
        self.ruedas = ruedas

    def __str__(self):
        return f"Vehículo con {self.ruedas} ruedas"

class Coche(Vehiculo):
    def __init__(self):
        super().__init__(4)

class Camion(Vehiculo):
    def __init__(self):
        super().__init__(6)

class Motocicleta(Vehiculo):
    def __init__(self):
        super().__init__(2)

class Bicicleta(Vehiculo):
    def __init__(self):
        super().__init__(2)

def catalogar(vehiculos, ruedas=None):
    if ruedas is not None:
        vehiculos_filtrados = [vehiculo for vehiculo in vehiculos if vehiculo.ruedas == ruedas]
        print(f"Se han encontrado {len(vehiculos_filtrados)} vehículos con {ruedas} ruedas:")
        for vehiculo in vehiculos_filtrados:
            print(vehiculo)
    else:
        print(f"Se han encontrado {len(vehiculos)} vehículos:")
        for vehiculo in vehiculos:
            print(vehiculo)

# Ejemplo de uso
vehiculos = [Vehiculo(2), Vehiculo(4), Vehiculo(4), Vehiculo(3)]
catalogar(vehiculos, 4)
catalogar(vehiculos)