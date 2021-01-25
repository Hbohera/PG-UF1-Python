def main():
    numsec = int(input("Introduce el número de segundos: "))  # El usuario tendrá que introducir el número de segundos que quiere convertir y lo convertimos en entero.
    while numsec < 0:  # Validamos que el número introducido no sea negativo.
        numsec = int(input("Introduce el número de segundos: "))
    days, daysaux = divmod(numsec, 86400)  # Calculamos el número de días.
    hours, hoursaux = divmod(daysaux, 3600)  # Calculamos el número de horas.
    minutes, seconds = divmod(hoursaux, 60)  # Calculamos el número de minutos y segundos.
    print()  # Mostramos un salto de línea.
    print(numsec, "segundos son:", days, 'días,', hours, 'horas,', minutes, 'minutos,', seconds, 'segundos.')  # Se mostrará el resultado de n segundos en días, horas, minutos y segundos.

if __name__ == "__main__":
    main()