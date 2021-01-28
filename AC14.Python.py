def main():
    number_list = []  # Iniciamos la lista que contendrá los números introducidos por el usuario.
    times = int(input("¿Cuantos números quieres introducir?: "))  # Le pedimos al usuario cuantas veces quiere introducir un número.
    for i in range(times):  # Tantas veces como quiera introducira un número.
        number = int(input("Introduce el número: "))  # Le pedimos el número.
        while number < 0:  # Validamos que sea un número entero.
            number = int(input("Introduce el número: "))  # Si no es entero le pedira el valor hasta que lo sea.
        number_list.append(number)  # Añadimos el valor en el final de la lista.
    print("\nLa suma total es:", sum(number_list))  # Mostramos al usuario la suma total de los números que contiene la lista.

if __name__ == "__main__":
    main()