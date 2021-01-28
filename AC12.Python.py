NUMBERS = 10
def main():
    count_e = 0  # Contador de números pares.
    count_o = 0  # Contador de números impares.
    number_list = []  # Lista que gurdará los números introducidos.
    even = []  # Lista que guardará los números pares.
    odd = []  # Lista que guardará los números impares.
    for i in range(NUMBERS):  # Pedimos tantas veces como el enunciado ha establecido.
        number = int(input("Introduce el número: "))  # La variable number almacenará el número introducido por el usuario.
        while number < 0 or number > 10:  # Verificamos que el número introducido este dentro del rango aceptado.
            number = int(input("Introduce el número entre 0 y 10 incluidos: "))  # Si no es así, se lo pedimos de nuevo.
        number_list.append(number) # Una vez tengamos el número validado, lo añadimos al final de la lista.
    for i in range(NUMBERS):
        if number_list[i] % 2 == 0:  # Comprobamos si el primer número introducido es par, y asi sucesivamente.
            even.append(number_list[i])  # Guardamos el valor en la lista de pares.
            count_e += 1  # Incrementamos el contador.
        else:  # Si el primer número introducido es impar lo guardará en su respectiva lista.
            odd.append(number_list[i])  # Guardamos el valor en la lista de impares.
            count_o += 1  # Incrementamos el contador.
    print("\nLos números pares son:", end=" ")
    for i in range(count_e):
        print(even[i], end=" ")  # Mostramos al usuario la lista con los números pares.
    print("\nLos números impares son:", end=" ")
    for j in range(count_o):
        print(odd[j], end=" ")  # Mostramos al usuario la lista con los números impares.

if __name__ == "__main__":
    main()