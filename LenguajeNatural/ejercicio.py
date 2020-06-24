entrada = float(input("Entre el precio de entrada: "))
descuento = []

for i in range(0,6):
    valor = entrada * 0.10
    entrada = entrada - valor
    descuento.append(entrada)

for i in range (0, len(descuento)):
    print("Elemento " + str(i) + ": " + str(descuento[i]))