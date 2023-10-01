cantidad_invertir = float(input("Introduce la cantidad a invertir: "))
interes_anual = float(input("Introduce el interés anual (%): "))
interes_decimal = interes_anual / 100
num_años = int(input("Introduce el número de años: "))
capital_obtenido = cantidad_invertir * (1 + interes_decimal)**num_años
print("El capital obtenido en la inversión es: €" + str(capital_obtenido))
input("pulsa enter para salir")