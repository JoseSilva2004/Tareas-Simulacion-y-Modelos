import random

#parámetros
probabilidad_exito = 0.4
costo_exploracion = 1_000_000
cantidad_barriles = 300_000
precio_barril = 150

#Calculo de ingresos y perdidas
def calcular_ingresos():
    if random.random() < probabilidad_exito:
        ingresos_totales = cantidad_barriles * precio_barril
        ingresos_empresa = ingresos_totales * 0.6
        ingresos_estado = ingresos_totales * 0.4
        return ingresos_empresa - costo_exploracion, ingresos_estado
    else:
        return -costo_exploracion, 0

#Simulacion de múltiples exploraciones
num_simulaciones = 10000
resultados_empresa = []
ingresos_estado_total = 0

for _ in range(num_simulaciones):
    resultado_empresa, ingresos_estado = calcular_ingresos()
    resultados_empresa.append(resultado_empresa)
    ingresos_estado_total += ingresos_estado

#Análidis de resultados
exito = sum(1 for resultado in resultados_empresa if resultado > 0)
fracaso = num_simulaciones - exito
promedio_ganancia_empresa = sum(resultados_empresa) / num_simulaciones
promedio_ingresos_estado = ingresos_estado_total / num_simulaciones

# Formatear la salida con separadores de miles
print(f"Cantidad de exploraciones: {num_simulaciones:,}")
print(f"Tasa de éxito: {exito / num_simulaciones * 100:.2f}%")
print(f"Tasa de fracaso: {fracaso / num_simulaciones * 100:.2f}%")
print(f"Promedio de ganancia/pérdida para la empresa: ${promedio_ganancia_empresa:,.2f}")
print(f"Promedio de ingresos para el estado: ${promedio_ingresos_estado:,.2f}")
