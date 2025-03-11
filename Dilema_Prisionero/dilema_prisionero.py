import random

# Definimos la recompensa para cada combinación de decisiones
recompensa = {
    ('confesar', 'confesar'): (5, 5),
    ('confesar', 'no confesar'): (0, 10),
    ('no confesar', 'confesar'): (10, 0),
    ('no confesar', 'no confesar'): (1, 1)
}

# Función para jugar una ronda del dilema del prisionero
def jugar(decision1, decision2):
    return recompensa[(decision1, decision2)]

# Función para simular múltiples rondas del dilema del prisionero
def simular_rondas(num_rondas):
    resultados = []
    for i in range(num_rondas):
        # Generamos decisiones aleatorias para ambos prisioneros
        decision_prisionero1 = random.choice(['confesar', 'no confesar'])
        decision_prisionero2 = random.choice(['confesar', 'no confesar'])
        
        # Jugamos la ronda y obtenemos el resultado
        resultado = jugar(decision_prisionero1, decision_prisionero2)
        resultados.append(resultado)
        
        # Imprimimos el resultado de la ronda
        print(f"Ronda {i+1}: Prisionero 1 elige {decision_prisionero1}, Prisionero 2 elige {decision_prisionero2}")
        print(f"Resultado: Prisionero 1: {resultado[0]} años, Prisionero 2: {resultado[1]} años\n")
    
    return resultados

# Número de rondas a simular
num_rondas = 5  # numero de rondas a simular

# Ejecutamos la simulación
resultados_simulacion = simular_rondas(num_rondas)

# Resumen de los resultados
print("\nResumen de la simulación:")
for i, resultado in enumerate(resultados_simulacion):
    print(f"Ronda {i+1}: Prisionero 1: {resultado[0]} años, Prisionero 2: {resultado[1]} años")