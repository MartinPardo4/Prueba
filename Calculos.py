def distanciaMru(tiempo, velocidad):
    return velocidad * tiempo
def tiempoMru(velocidad, distancia):
    return distancia/velocidad
def velocidadMru(tiempo, distancia):
    return distancia/tiempo
def switch(case):
    if case == 1:
        tiempo = int(input("Ingrese el tiempo (segundos): "))
        velocidad = int(input("Ingrese la velocidad (metros/segundos): "))
        return str(distanciaMru(tiempo, velocidad)) + " metros"
    elif case == 2:
        velocidad = int(input("Ingrese la velocidad (metros/segundos): "))
        distancia = int(input("Ingrese la distancia (metros): "))
        return str(tiempoMru(velocidad, distancia)) + " segundos"
    elif case == 3:
        tiempo = int(input("Ingrese el tiempo (segundos): "))
        distancia = int(input("Ingrese la distancia (metros): "))
        return str(velocidadMru(tiempo, distancia)) + " metros por segundos"

x = int(input("Qué quiere calcular?\n(distancia(1)/tiempo(2)/velocidad(3)): "))
resultado = switch(x)
print("RESULTADO: " + resultado)