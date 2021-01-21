def main():
    number=int(input("Introduce un número entre 1 y 10: ")) # Variable que guardará el primer número
    while number < 1 or number > 10: # Si el primer número no cumple la condición le volvera a pedirlo hasta que la cumpla
        number=int(input("Introduce un número entre 1 y 10: "))
    print("El número introducido esta dentro del rango") # Se mostrará al usuario que ha introducido correctamente el número

if __name__ == "__main__":
    main()