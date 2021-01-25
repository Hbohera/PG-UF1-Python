LINES = 7
def main():
    x = 1  # Declaramos la variable x que servira como contador.
    aux = 0  # Declaramos la variable aux con valor 0.
    count = 2  # Declaramos la variable que mostrará los números ascendente empezando por 2.
    for i in range(LINES):  # Se repitirá la acción tantas veces como valga la variable LINES(7).
        aux = x  # Declaramos la variable aux como auxiliar de x.
        for j in range (LINES-aux):
            print(" ", end=" ")  # Se imprimirán espacios por los números que aun no se han mostrado.
        for k in range(x):
            print(aux, end=" ")  # Se mostrará la línea descendente de números cada vez sumando uno mas.
            aux -= 1  # Le restamos el valor a la variable aux.
        for h in range(x-1):
            print(count, end=" ") # Mostrará la línea ascendente comenzando por 2.
            count += 1 # Incrementara el valor cada vez que se ejecute.
        x += 1  # Incrementamos el valor de x.
        count = 2  # Reseteamos el valor de la variable count.
        aux -= 1  # Reducimos el valor de la variable aux.
        print()  # Mostrará un salto de línea
    x = LINES - 1  # Cambiamos el valor de x para que empieze desde el número anterior a su valor.
    aux = 0
    count = 2
    for i in range(LINES-1):  # Realizará la acción tantas veces como la variable LINES valga y restandole uno.
        aux = x
        for j in range (LINES-aux):
            print(" ", end=" ")  # Se imprimirán espacios por los números que aun no se han mostrado.
        for k in range(x):
            print(aux, end=" ")  # Se mostrará la línea descendente de números cada vez sumando uno mas.
            aux -= 1
        for h in range(x-1):
            print(count, end=" ")  # Mostrará la línea ascendente comenzando por 2.
            count += 1
        print()  # Mostrará un salto de línea
        x -= 1  # Reducimos el valor de x en este caso, para imprimir la parte de abajo del diamante.
        count = 2
        aux -= 1

if __name__ == "__main__":
    main()