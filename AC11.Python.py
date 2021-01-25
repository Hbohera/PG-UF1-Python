APPROVED = 5  # La variable de aprobado tendrá de valor un 5.
SIZE = 15  # Variable que contiene el número de alumnos que necesitamos saber su nota.
def main():
    sum_p = 0  # Inicializamos la variable con un valor de 0.
    sum_f = 0  # Inicializamos la variable con un valor de 0.
    count_p = 0  # Inicializamos la variable con un valor de 0.
    count_f = 0  # Inicializamos la variable con un valor de 0.
    for i in range(SIZE):
        notes = int(input("Introduce la nota del alumno: "))  # Pedimos al usuario la nota del alumno.
        while notes < 0 or notes > 10:  # Validamos que sea entre 0 y 10.
            notes = int(input("Introduce la nota del alumno: "))
        if notes >= APPROVED:  # Si la nota introducida es mayor o igual que 5.
            count_p += 1  # Sumará uno al contador de aprobados.
            sum_p = notes + sum_p # Ira sumando los valores introducidos por teclado.
        else:  # Si no entra en el if, entrará al else.
            count_f += 1  # Sumará uno al contador de suspensos.
            sum_f = notes + sum_f  # Ira sumando los valores de los suspensos.
    average_p = sum_p / count_p  # Realizará la media de aprobados.
    average_f = sum_f / count_f  # Realizará la media de suspensos.
    print()
    print("Hay", count_f, "suspensos")  # Mostrará el total de suspensos.
    print(f"Y la media de suspensos es: {average_f:.2f}")  # Mostrará la media de suspensos.
    print()
    print("Hay", count_p, "aprobados")  # Mostrará el total de aprobados.
    print(f"Y la media de aprobados es: {average_p:.2f}")  # Mostrará la media de aprobados.

if __name__ == "__main__":
    main()