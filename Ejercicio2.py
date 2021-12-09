APPROVED = 5
def main():
    size = int(input("Introduce cuantas notas quieres pedir: "))
    while size < 0:
        size = int(input("Vuelve a introducir cuantas notas quieres pedir: "))
    sum_p = 0
    sum_f = 0
    count_p = 0
    count_f = 0
    for i in range(size):
        notes = int(input("Introduce la nota del alumno: "))
        while notes < 0 or notes > 10:
            notes = int(input("Introduce la nota del alumno entre 0 y 10(incluidos): "))
        if notes >= APPROVED:
            count_p += 1
            sum_p = notes + sum_p
        else:
            count_f += 1
            sum_f = notes + sum_f
    average_p = sum_p / count_p
    average_f = sum_f / count_f
    print()
    print("Hay", count_f, "suspensos")
    print(f"Y la media de suspensos es: {average_f:.2f}")
    print()
    print("Hay", count_p, "aprobados")
    print(f"Y la media de aprobados es: {average_p:.2f}")

if __name__ == "__main__":
    main()
