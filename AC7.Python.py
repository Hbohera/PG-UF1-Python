def main():
    num1 = int(input("Introduce el primer número: ")) # El usuario introduce el primer número
    num2 = int(input("Introduce el segundo número: ")) # El usuario introduce el segundo número
    num3 = int(input("Introduce el tercer número: ")) # El usuario introduce el tercer número
    sum = num1 + num2 + num3 # Se suma todos los números y se guarda en una variable
    if num1 == num2: # Verifica si el primer número es igual al segundo
        if num2 == num3: # Si es igual al segundo mira si el segundo es igual al tercero
            sum = sum * 3 # Si es asi la suma la múltiplica por tres
            print("El total de su suma multiplicada por tres es:", sum) # Muestra al usuario el resultado de la suma y de la multiplicación
        else:
            print("El total de su suma es:", sum) # Muestra al usuario el resultado de la suma
    else:
        print("El total de su suma es:", sum) # Muestra al usuario el resultado de la suma
        
    
if __name__ == "__main__":
    main()