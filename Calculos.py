def distanciaMru(tiempo, velocidad):
    return velocidad * tiempo
def tiempoMru(velocidad, distancia):
    return distancia/velocidad
def velocidadMru(tiempo, distancia):
    return distancia/tiempo
def distanciaMruv(velocidadF, aceleracion):
    return velocidadF**2/(2*aceleracion)
#switch
def switch(case, accion1, accion2, accion3):
    if case == 1:
        return accion1()
    elif case == 2:
        return accion2()
    elif case == 3:
        return accion3()

def caso1():
    tiempo = int(input("Ingrese el tiempo (segundos): "))
    velocidad = int(input("Ingrese la velocidad (metros/segundos): "))
    return str(distanciaMru(tiempo, velocidad)) + " metros"
def caso2():
    velocidad = int(input("Ingrese la velocidad (metros/segundos): "))
    distancia = int(input("Ingrese la distancia (metros): "))
    return str(tiempoMru(velocidad, distancia)) + " segundos"
def caso3():
    tiempo = int(input("Ingrese el tiempo (segundos): "))
    distancia = int(input("Ingrese la distancia (metros): "))
    return str(velocidadMru(tiempo, distancia)) + " metros por segundos"

def decidir(case):
    return switch(case, caso1, caso2, caso3)

#opcion = int(input(""))
x = int(input("Qué quiere calcular?\n(distancia(1)/tiempo(2)/velocidad(3)): "))
resultado = decidir(x)
print("RESULTADO: " + resultado)