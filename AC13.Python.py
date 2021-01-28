def main():
    num1 = int(input("Introduce el primer número: "))  # Pedimos al usuario que introduza el primer número.
    while num1 < 0:  # Validamos que sea de tipo entero.
        num1 = int(input("Introduce el primer número: "))
    num2 = int(input("Introduce el segundo número: "))  # Pedimos al usuario que introduza el segundo número.
    while num2 < 0:  # Validamos que sea de tipo entero.
        num2 = int(input("Introduce el segundo número: "))
    num1, num2 = num2, num1  # Hacemos el intercambio de valores.
    print("\nEl primer ńumero que has introducido este:", num1)  # Mostramos al usuario el intercambio.
    print("El segundo ńumero que has introducido este:", num2)
    print("\nOuch!", "Hubo un error y los números se han intercambiado!")

if __name__ == "__main__":
    main()