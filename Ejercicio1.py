def main():
    n1 = int(input("Introduce el primer número: "))
    while n1 < 0:
        n1 = int(input("Vuelve a introducir el número: "))
    n2 = int(input("Introduce el segundo número: "))
    while n2 < 0:
        n2 = int(input("Vuelve a introducir el número: "))
    numbers = list()
    numbers.append(n1)
    numbers.append(n2)
    if numbers[0] < numbers[1]:
        print("El primero número es mas pequeño que el segundo.")
    else:
        print("Error: El segundo número es mas pequeño que el primero")
    numbers.sort()
    print(numbers)

if __name__ == "__main__":
    main()
