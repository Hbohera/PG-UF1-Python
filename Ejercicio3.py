def main():
    repeat= int(input("¿Cuantos usuarios quieres introducir?: "))
    username = list()
    departament = list()
    classroom = list()
    for i in range(repeat):
        username.append(str(input("\n¿Cual es el nombre del alumno?: ")))
        departament.append(str(input("¿Cual es el nombre del departamento?: ")))
        classroom.append(int(input("¿Que número tiene la clase?: ")))
        while 1 < classroom[-1] > 15:
            classroom.append(int(input("¿Vuelve a introducir el número que tiene la clase?(1-15): ")))
    students = {
        "username": username,
        "departament": departament,
        "classroom": classroom
    }
    for y in students:
            print("\n |", students[y], end=" | \n")

if __name__ == "__main__":
    main()
