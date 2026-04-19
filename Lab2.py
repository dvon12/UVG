participantes = 0
def daño():
    daño = (ATA + poder - DEF) * mult_tipo
    return daño
def menu():
    print("1. Agregar particpantes")
    print("2. Seleccione el pokemon")
pokemon = [
    {"Name": "Bulbasaur", "Tipo": "Planta", "HP": 95, "ATA": 55, "DEF": 50},
    {"Name": "Charmander", "Tipo": "Fuego", "HP": 70, "ATA": 80, "DEF": 50},
    {"Name": "Squirtle", "Tipo": "Agua", "HP": 60, "ATA": 60, "DEF": 80},
    {"Name": "Leafon", "Tipo": "Planta", "HP": 70, "ATA": 80, "DEF": 60},
    {"Name": "Vaporeon", "Tipo": "Agua", "HP": 130, "ATA": 65, "DEF": 60},
    {"Name": "Flareon", "Tipo": "Fuego", "HP": 65, "ATA": 130, "DEF": 60},
]
nombres = []
opcion = 1
while opcion != 0:
    menu()
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        participantes = int(input("Ingrese el numero de participantes: "))
        if (participantes /2) == int:
            for i in range(participantes):
                nombre = input("Ingrese el nombre del participante: ")
                nombres.append(nombre)