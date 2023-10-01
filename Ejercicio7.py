peso = float(input("Introduce tu peso en kg: "))
estatura = float(input("Introduce tu estatura en metros: "))
imc = peso / (estatura ** 2)
imc = int(imc * 100) / 100
print("Tu índice de masa corporal es", imc)
input("Pulsa enter para salir")