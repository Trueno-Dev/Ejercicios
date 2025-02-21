## JUEGOS OLIMPICOS 2024    

import random

ganadores_list = []
eventos = []
participantes = []
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
    for _ in range(contador):
        nombre = str(input("Nombre del evento: "))
        eventos.append(nombre)
        print("Evento añadido con exito")
    return eventos

def juegos_olimpicos():
    for participante in participantes:
        medalla_ganadora = random.choice(medallas)
        evento_ganador = random.choice(eventos)

        ganador = {
        "nombre": participante['nombre'],
        "pais": participante['pais'],
        "medalla": medalla_ganadora,
        "evento": evento_ganador
        }

        ganadores_list.append(ganador)

def mostrar_ganadores():
    print("\nResultados de los Juegos Olímpicos 2024:")
    for i, ganador in enumerate(ganadores_list, start=1):
        print(f"Ganador {i}: {ganador['nombre']} de {ganador['pais']} ganó la medalla de {ganador['medalla']} en el evento de {ganador['evento']}")




registrar_eventos()
agregar_participantes()
juegos_olimpicos()
mostrar_ganadores()