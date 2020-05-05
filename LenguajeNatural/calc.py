from math import sqrt

entrada = -999999999
while (entrada != 6):
    print("#########################################################################################")
    print("La ultra mega calculadora que al final no sabemos bien que vergas hace buajaja ")
    print("Opcion 1: Sumar")
    print("Opcion 2: Restar")
    print("Opcion 3: Multiplicar")
    print("opcion 4: Dividir")
    print("opcion 5: Raiz cuadrada")
    print("Opcion 6: Me fui a jugar wow")
    print("#########################################################################################")

    entrada = input("Entre la opcion:")
    if (entrada < 1 and entrada > 6):
        print("No seas imbecil")
    if (entrada == 1):
        num1 = input("Entre primer numero")
        num2 = input("El otro numero")
        print("La suma es " + str(num1 + num2))
    if (entrada == 2):
        num1 = input("Entre primer numero")
        num2 = input("El otro numero")
        print("La resta es " + str(num1 - num2))
    if (entrada == 3):
        num1 = input("Entre primer numero")
        num2 = input("El otro numero")
        print("La multiplicacion es " + str(num1 * num2))
    if (entrada == 4):
        num1 = input("Entre primer numero")
        num2 = input("El otro numero")
        print("La division es " + str(num1 / num2))
    if (entrada == 5):
        num1 = input("Entre primer numero")
        num2 = input("El otro numero")
        print("La raiz es " + str(sqrt(num1)))