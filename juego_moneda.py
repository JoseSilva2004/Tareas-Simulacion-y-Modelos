import random
#def generar_simulacion(n):
    #Est = []

    #for _ in range(n):
        #r = random.randint(0,1)

       # if r < 0.50:
      #      Est.append('a')
     #   elif r < 0.80:
    #        Est.append('b')
   #     else:
  #          Est.append('c')
 #   return Est


#print(generar_simulacion(2))


#Funcion para tirar un dado

def tirar_dado():   
    return random.randint(1,6)  ##Devuelve un numero aleatorio entre 1 y 6 (caras del dado)

def tirar_moneda():
    return random.choice(['cara', 'cruz'])  #Retorna un string que seria la cara de la moneda

def jugar(apuesta_inicial, num_tiradas):    #Recibe la apuesta inicial y los intentos
    ganancias = 0  
    apuesta = apuesta_inicial
    resultados = {'ganar': 0, 'perder': 0}  #Diccionario para llevar la cuenta de las veces que el usuario perdió o ganó

    for _ in range(num_tiradas): 
        dado = tirar_dado() #Se tira el dado
        moneda = tirar_moneda() #Se tira la moneda

        if moneda == 'cara' and dado % 2 == 0:  #Si la moneda es cara y el dado es par
            ganancias += apuesta * 2    #Se duplica la apuesta
            resultados['ganar'] += 1
            apuesta = apuesta_inicial / 2   #Se divide por la mitad la apuesta inicial
        
        else:   
            ganancias -= apuesta
            resultados['perder'] += 1
            apuesta *= 2    #Se duplica la apuesta
    return ganancias, resultados


if __name__ == "__main__":
    apuesta_inicial = int(input("Ingrese la apuesta inicial: "))
    num_tiradas = int(input("Ingrese el numero de tiradas: "))

    #Ejecutar el juego
    ganancias, resultados = jugar(apuesta_inicial, num_tiradas)

    print(f"\nGanancias totales: {ganancias}")
    print(f"Veces ganadas: {resultados['ganar']} ({resultados['ganar'] / num_tiradas * 100}%)")
    print(f"Veces perdidas: {resultados['perder']} ({resultados['perder'] / num_tiradas * 100}%)")