n = int(input("Introduce un número positivo: "))
if n <= 0:
    print("El número que acabas de instroducir no es positivo")
else:
    suma = (n * (n + 1)) // 2
    print("La suma de los enteros desde 1 hasta", n, "es:", suma)
input("pulsa enter para salir")
