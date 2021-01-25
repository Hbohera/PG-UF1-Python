NUMBERS = 10
def main():
    number_list = []
    count_e = 0
    count_o = 0

    for i in range(NUMBERS):
        number_list[i] = int(input("Introduce el número"))
        while number_list[i] < 0 or number_list[i] > 10:
            number_list[i] = int(input("Introduce el número entre 0 y 10 incluidos: "))
    for i in range(NUMBERS):
        if number_list[i] MOD 2 == 0:
            even[count_e] = numbers_list[i]
            count_e += 1
        else
if __name__ == "__main__":
    main()