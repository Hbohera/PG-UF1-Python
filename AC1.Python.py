def main():
    lista = int(input("¿Hasta qué número quieres que sea el intervalo?: ")) # Variable que contiene el número final del intervalo
    count = 0 # Variable contador
    for i in range(2, lista + 1):
        primos = True # Inicializamos la variable primos por defecto en True
        for j in range(2,11): 
            if i == j:
               break
            elif i%j == 0: # Si el número se puede dividir entre otro número dara falso.
               primos = False
            else:
               continue
        if primos == True:
            print(' ',i, end='') # Mostramos los números primos
            count += 1
            
            
if __name__ == "__main__":
    main()
