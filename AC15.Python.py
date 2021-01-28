def main():
    a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]  # Declaramos la lista con los números.
    b = list()  # Creamos una lista vacía que guardara los números que no se repitan.
    for i in a:  # Dentro de la lista a.
        if i not in b:  # Validamos que no se repita ningún número.
            b.append(i)  # Lo guardamos dentro de la lista b.
    print("La lista sin repeticiones es esta:", end=" ")  # Mostramos al usuario la lista sin repeticiones.
    for i in b:
        print(i, end=" ")

if __name__ == "__main__":
    main()