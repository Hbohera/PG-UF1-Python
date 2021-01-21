def main():
    sum = 0 # Variable que hara de auxiliar del número.
    for i in range(10):
        number= float(input("Introduce el número: ")) # Introduce el número por teclado.
        sum += number # El número se va sumando a los siguientes hasta 10.
    sum = sum / 10 # Dividimos el total de la suma entre el total de números que hay.
    print("La media de todos los números es:", sum) # Se mostrará al usuario la media de todos los números.
            
if __name__ == "__main__":
    main()