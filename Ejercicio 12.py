precio_pan = 3.49 
descuento = 60 
barras_no_frescas = int(input("Introduce el número de barras de pan vendidas sin ser del día: "))
precio_total_normal= barras_no_frescas * precio_pan
descuento_aplicado = (descuento / 100) * precio_total_normal
ganancia_total = precio_total_normal - descuento_aplicado
print("Precio habitual de una barra de pan: €", precio_pan)
print("Descuento por no ser fresca: {} %".format(descuento))
print("Ganancia final total: €", ganancia_total)
input("pulsa enter para salir")