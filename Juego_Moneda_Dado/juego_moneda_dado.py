import random

def tirar_dado():   
    return random.randint(1, 6)  # Devuelve un número aleatorio entre 1 y 6 (caras del dado)

def tirar_moneda():
    return random.choice(['cara', 'cruz'])  # Retorna un string que sería la cara de la moneda

def jugar(apuesta_inicial, num_tiradas):    # Recibe la apuesta inicial y los intentos
    ganancias = 0  
    apuesta = apuesta_inicial
    resultados = {'ganar': 0, 'perder': 0}  # Diccionario para llevar la cuenta de las veces que el usuario perdió o ganó
    dinero_invertido = apuesta_inicial * num_tiradas  # Dinero total invertido
    dinero_gastado = 0  # Dinero gastado en apuestas perdidas
    dinero_ganado = 0   # Dinero ganado en apuestas ganadas

    for _ in range(num_tiradas): 
        dado = tirar_dado() # Se tira el dado
        moneda = tirar_moneda() # Se tira la moneda

        if moneda == 'cara' and dado % 2 == 0:  # Si la moneda es cara y el dado es par
            ganancias += apuesta * 2    # Se duplica la apuesta
            resultados['ganar'] += 1
            dinero_ganado += apuesta * 2  # Se suma el dinero ganado
            apuesta = apuesta_inicial / 2   # Se divide por la mitad la apuesta inicial
        
        else:   
            ganancias -= apuesta
            resultados['perder'] += 1
            dinero_gastado += apuesta  # Se suma el dinero gastado
            apuesta *= 2    # Se duplica la apuesta

    return ganancias, resultados, dinero_invertido, dinero_gastado, dinero_ganado

# Función para validar la entrada del usuario
def validar_entrada(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor <= 0:  # Asegurarse de que el valor sea positivo
                print("Error: Ingrese un número mayor que 0.")
            else:
                return valor
        except ValueError:  # Capturar errores si no se ingresa un número
            print("Error: Ingrese un número entero válido.")


if __name__ == "__main__":
    apuesta_inicial = 10000
    num_tiradas = validar_entrada("Ingrese el número de tiradas: ")

    # Ejecutar el juego
    ganancias, resultados, dinero_invertido, dinero_gastado, dinero_ganado = jugar(apuesta_inicial, num_tiradas)

    # Imprimir la salida
    print(f"\nDinero invertido: {dinero_invertido:,}$")
    print(f"Dinero gastado: {dinero_gastado:,}$")
    print(f"Dinero ganado: {dinero_ganado:,}$")
    print(f"Ganancias totales: {ganancias:,}$")
    print(f"Veces ganadas: {resultados['ganar']} ({resultados['ganar'] / num_tiradas * 100:.2f}%)")
    print(f"Veces perdidas: {resultados['perder']} ({resultados['perder'] / num_tiradas * 100:.2f}%)")