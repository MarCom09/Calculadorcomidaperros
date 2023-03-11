import time
print('Hola, vamos a calcular cuanto debe comer al dia y en raciones tu perr@. Empecemos.')
time.sleep(1)

# Pedimos al usuario que ingrese el peso del perro en kilogramos
peso_perro = float(input("Ingrese el peso del perro en kilogramos: "))

# Pedimos al usuario que ingrese la cantidad de raciones diarias del perro.
cantidad_raciones = float(input('Ingrese el numero de raciones que el perro va a tomar: '))


# Definimos la cantidad de comida que debe consumir el perro por cada kilogramo de peso
comida_por_kilo = 20 # 20 gramos de comida por kilo de peso

# Calculamos la cantidad de comida diaria que debe consumir el perro
cantidad_comida = comida_por_kilo * peso_perro

# Calculamos la cantidad de comida por ración que debe consumir el perro
comida_por_racion = cantidad_comida // cantidad_raciones

#Presentamos el resultado en pantalla
print(f'Su perro de {peso_perro} kilos debe comer {cantidad_comida} gramos de comida al día o {comida_por_racion} en {cantidad_raciones} raciones.')
