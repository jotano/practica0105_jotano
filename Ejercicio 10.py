#Peso en gramos
peso_payaso = 112
peso_muñeca = 75
num_payasos = int(input("Número de payasos vendidos: "))
num_munecas = int(input("Número de muñecas vendidas: "))
peso_total = (num_payasos * peso_payaso) + (num_munecas * peso_muñeca)
print("El peso total del paquete que será enviado es de " + str(peso_total) + " gramos.")
input("pulsa enter para salir")
