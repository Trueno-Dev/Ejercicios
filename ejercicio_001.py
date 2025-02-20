## JUEGOS OLIMPICOS 2024    

from random import randint


eventos = [
]

participantes = [
]

medallas = ["oro", "plata", "bronce"]


def agregar_participantes():
    
    contador_participantes = int(input("¿Cuántos participantes deseas añadir? \n"))
    
    for _ in range(contador_participantes):
        nombre = input("Nombre del participante: ")
        pais = input("País del participante: ")
        participantes.append({"nombre": nombre, "pais": pais})
        print("Participante añadido con éxito")
    
    return participantes

def registrar_eventos():
    contador = int(input("¿Cuántos Eventos, desea agregar? \n"))
    for i in range(contador):
        nombre = str(input("Nombre del evento: "))
        eventos.append(nombre)
        print("Evento añadido con exito")

def ganador():
    participantes[0]["nombre"]
    participantes[0]["pais"]
    medallas[0]
    eventos[0]
    print(f"El ganador de la medalla de {medallas[0]} en el evento {eventos[0]} es: {participantes[0]['nombre']} de {participantes[0]['pais']}")


#registrar_eventos()

agregar_participantes()


#ganador()

