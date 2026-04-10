#Josué Ajú y Diego Barrera
playlist = [] #Lista vacía para almacenar las canciones
def obtener_votos(cancion): #Función para obtener el número de votos de una canción, se usa para encontrar la canción más votada
    return cancion["votos"]
def menu():
    print("---Menú Principal---")
    print("1. Agregar canción")
    print("2. Eliminar canción")
    print("3. Votar canción")
    print("4. Ver playlist")
    print("5. Buscar canción por artista")
    print("6. Ver canción más votada")
    print("7. Salir")


opcion = 0

while opcion != 7: #Bucle principal del programa, se ejecuta hasta que el usuario seleccione la opción de salir
    menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1: #Agregar canción
            cancion = input("Ingrese el nombre de la canción: ")
            artista = input("Ingrese el nombre del artista: ")
            nueva = {"cancion": cancion, "artista": artista, "votos": 0} #Diccionario para almacenar la información de la canción
            playlist.append(nueva) #Agrega la nueva canción a la playlist, modificando la lista original. Sin necesidad de un diccionario adicional para almacenar las canciones.
            print("Canción agregada correctamente.")
    elif opcion == 2:
        cancion = input("Ingrese el nombre de la canción a eliminar: ")
        artista = input("Ingrese el nombre del artista de la canción a eliminar: ")
        for song in playlist: 
            if song["cancion"].lower() == cancion.lower() and song["artista"].lower() == artista.lower(): #Busca la canción en la playlist, si la encuentra, la elimina y sale del bucle. Si no la encuentra, muestra un mensaje indicando que no se encontró la canción.
                playlist.remove(song)
                print("Canción eliminada correctamente.")
                break
        else:
            print("Canción no encontrada.")

    elif opcion == 3:
            votar = input("Ingrese el nombre de la canción a votar: ")
            artista = input("Ingrese el nombre del artista de la canción a votar: ")
            for song in playlist:
                if song["cancion"].lower() == votar.lower() and song["artista"].lower() == artista.lower(): #Busca la canción en la playlist, si la encuentra, incrementa su contador de votos y sale del bucle. Si no la encuentra, muestra un mensaje indicando que no se encontró la canción.
                    song["votos"] += 1 #Suma un voto a la canción seleccionada.
                    print("Voto registrado correctamente.")
                    break
            else:
                print("Canción no encontrada.")
    elif opcion == 4:
            if not playlist: #Verifica si la playlist está vacía
                print("La playlist está vacia.")
            else:
                print("Playlist:")
                for song in playlist: #Muestra cada canción en la playlist con su artista y número de votos.
                    print(f"- {song['cancion']} de {song['artista']} con {song['votos']} votos.")
    elif opcion == 5:
            artista = input("Ingrese el nombre del artista: ")
            canciones = [song for song in playlist if song["artista"].lower() == artista.lower()] #Busca todas las canciones del artista ingresado en la playlist y las almacena en una lista. Si no se encuentran canciones del artista, muestra un mensaje indicando que no se encontraron canciones.
            if canciones:
                print(f"Canciones de {artista}:")
                for song in canciones:
                    print(f"- {song['cancion']} ({song['votos']} votos)")
            else:
                print(f"No se encontraron canciones de {artista}.")

    elif opcion == 6:
        if not playlist:
            print("La playlist está vacia.")
        else:
            cancion_mas_votada = max(playlist, key=obtener_votos) #Utiliza la función max para encontrar la canción con el mayor número de votos en la playlist, utilizando la función obtener_votos como clave para comparar los votos de cada canción. Luego muestra la canción más votada con su artista y número de votos.
            print(f"Canción más votada: {cancion_mas_votada['cancion']} de {cancion_mas_votada['artista']} con {cancion_mas_votada['votos']} votos.")
    elif opcion == 7:
        print("Saliendo del programa...")

    else:
        print("Opción no válida. Intente nuevamente.")