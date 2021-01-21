def main():
    centimeters = float(input("Introduce los centímetros: ")) # Variable que almacená los CM introducidos por el usuario
    inches = (1/2.54) * centimeters # Se hace la conversión a pulgadas y se guarda en la variable inches
    print("La distancia en pulgadas es:", inches) # Se muestra el resultado al usuario
        
    
if __name__ == "__main__":
    main()