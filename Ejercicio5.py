#Diego Javier Barrera Boiton 26631
dia = ["Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado"] #Lista con los días de la semana
datos = [ #Lista para almacenar los datos de cada día, inicialmente con valores de 0
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]
]
#Variables para almacenar la opción del día, velocidad, temperatura, resultado de la sensación térmica y control de continuación
opcion = 0
velocidad = 0
temperatura = 0
resultado = 0
continuar = "Y"
#Función para solicitar al usuario la velocidad del viento y la temperatura
def velocidad_and_temperatura():
    velocidad = float(input("Ingrese la velocidad del viento en mi/h: "))
    temperatura = float(input("Ingrese la temperatura en grados Farenheit: "))
    return velocidad, temperatura
#Función para calcular la sensación térmica utilizando la fórmula dada
def calcular_sensacion_termica(velocidad, temperatura):
    W = 35.74 + (0.6215 * temperatura) - (35.75 * (velocidad ** 0.16)) + (0.4275 * temperatura * (velocidad ** 0.16))
    return W
#Función para convertir la temperatura de grados Farenheit a grados Celsius utilizando la fórmula dada
def temperatura_celsius(temperatura):
    C = (temperatura - 32) * 5.0/9.0
    return C
#Bucle principal para ingresar datos de cada día de la semana
while continuar == "Y":
    for i in range(7):
         print(i, dia[i])
    opcion = int(input("Seleccione el día de la semana (0-6): "))
    #Dependiendo de la opción seleccionada por el usuario, se solicita la velocidad y temperatura, se calcula la sensación térmica y se almacenan los datos en la lista "datos" en la posición correspondiente al día seleccionado
    if opcion == 0:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Domingo = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[0] = Domingo
    elif opcion == 1:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Lunes = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[1] = Lunes
    elif opcion == 2:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Martes = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[2] = Martes
    elif opcion == 3:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Miércoles = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[3] = Miércoles
    elif opcion == 4:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Jueves = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[4] = Jueves
    elif opcion == 5:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Viernes = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[5] = Viernes
    elif opcion == 6:
        registro = (velocidad_and_temperatura())
        print(f"La velocidad del viento es: {registro[0]} mi/h")
        print(f"La temperatura es: {registro[1]} °F")
        print(f"Sensación térmica: {calcular_sensacion_termica(registro[0], registro[1])}")
        print(f"Temperatura en Celsius: {temperatura_celsius(registro[1]):.2f} °C")
        Sábado = [registro[0], registro[1], calcular_sensacion_termica(registro[0], registro[1])]
        datos[6] = Sábado
    else:
        print("Opción inválida.")
    continuar = input("¿Desea ingresar datos para otro día? (Y/N): ")
    continuar = continuar.upper() #Si el usuario ingresa "y" en minúscula, se convierte a mayúscula para evitar errores de comparación 
    #Pude haber hecho lo de abajo pero para usar alguna funcion de lista
    if continuar == "N" or continuar == "n":
        break
    else:
        print("Opción inválida.")
#Lamento el uso excesivo de If, aun no me familiarizo con las listas
while resultado == 0: #Bucle para mostrar los datos de un día específico, se ejecuta mientras resultado sea igual a 0
    print("Seleccione el día que desea mostrar:") #Muestra los días de la semana para que el usuario seleccione uno

    for i in range(7):
            print(i, dia[i])

    mostrar = int(input("Ingrese el número del día: ")) #El usuario ingresa el número del día que desea mostrar, se asume que el usuario ingresará un número válido entre 0 y 6

    #Se muestra la información del día seleccionado, accediendo a los datos almacenados en la lista "datos" utilizando el índice correspondiente al día seleccionado por el usuario
    print("Datos del día seleccionado:")
    print("Día:", dia[mostrar])
    print("Velocidad:", datos[mostrar][0])
    print("Temperatura:", datos[mostrar][1])
    print("Sensación térmica:", datos[mostrar][2])
    print("Temperatura en Celsius:", temperatura_celsius(datos[mostrar][1]))


    resultado = input("Desea mostrar otro día? (Y/N): ") #Se pregunta al usuario si desea mostrar otro día, pero no se implementa la lógica para manejar la respuesta, por lo que el programa finalizará después de mostrar un día.
    if resultado == "Y" or resultado == "y":
        resultado = 0
    else:
        resultado = 1
print("Programa finalizado. Gracias por usarlo.")
