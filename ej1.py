#Ejercicio 1

varA = input("Ingrese una variable varA: ")
varB = input("Ingrese una variable varB: ")

try:
# Usando trycatch para manejar excepciones
    varA_int = int(varA)
    varB_int = int(varB)
    if isinstance(varA_int, int) and isinstance(varB_int, int):
    # Si varA es int AND varB es int
        if varA_int == varB_int:
            print("Variables iguales")
        else:
            if varA_int < varB_int:
                print("varA es más pequeño")
            if varA_int > varB_int:
                print("varA es más grande")

except:
    print("String involucrado")