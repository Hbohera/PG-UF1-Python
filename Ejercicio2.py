def main():
    repeat= int(input("¿Cuantas aulas quieres introducir?: "))
    aula = []
    nom_aula = []
    ip = []
    nombre_pcs = []
    for x in range(repeat):
        aula[x] = int(input("\n¿Cual es el número del aula?: "))
        while 1 < aula[x] > 50:
            aula[x] = int(input("\n¿Cual es el número del aula?(1-50): "))
        nom_aula[x] = str(input("¿Cual es el nombre del aula?: "))
        ip[x] = str(input("¿Cual es la IP del aula?: "))
        nombre_pcs[x] = int(input("¿Cuantos PC's hay en el aula?: "))
        while 1 < nombre_pcs[x] > 20:
            nombre_pcs[x] = int(input("¿Cuantos PC's hay en el aula?(1-20): "))
    classrooms = {
        "aula": aula,
        "nom_aula": nom_aula,
        "ip": ip,
        "nombre_pcs": nombre_pcs
    }
    for y in classrooms:
        for j in classrooms:
            print("\n |", classrooms[y][j], end=" | \n")

if __name__ == "__main__":
    main()