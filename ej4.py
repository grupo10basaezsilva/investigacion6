# Ejercicio 4

final = int(input("Ingrese un numero final deseado: "))
vectorResultante = 0
aux = 0
for n in range(1, final + 1):
# Por cada elemento (n) en el rango 1 -> final+1
# con n entero
    vectorResultante += n
    # El vector va sumando valores al iterar
    # Así se obtiene el resultado de la suma en vectorResultante
    aux += 1
    # Aux +1 por cada iteracion, esto ayuda a mostrar en
    # la forma solicitada el resultado
    if aux < final:
        print(n, end="+")
        # con end se puede especificar el valor final de la linea a imprimir
        # en caso de que no lleguemos al final, se muestra +
    else:
        print(n, end="=")
        # cuando lleguemos al elemento final se muestra =
# Finalmente imprimir el resultado
# concatenado a la suma anterior
print(vectorResultante)
