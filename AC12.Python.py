NUMBERS = 10
def main():
    count_e = 0
    count_o = 0
    number_list = []
    even = []
    odd = []
    for i in range(NUMBERS):
        number = int(input("Introduce el número: "))
        while number < 0 or number > 10:
            number = int(input("Introduce el número entre 0 y 10 incluidos: "))
        number_list.append(number)
    for i in range(NUMBERS):
        if number_list[i] % 2 == 0:
            even.append(number_list[i])
            count_e += 1
        else:
            odd.append(number_list[i])
            count_o += 1
    print()
    print("Los números pares son:", end=" ")
    for i in range(count_e):
        print(even[i], end=" ")
    print()
    print("Los números impares son:", end=" ")
    for j in range(count_o):
        print(odd[j], end=" ")

if __name__ == "__main__":
    main()