def main():
   mbytes = int(input("Introduce los MegaBytes: ")) # Variable que almacená los MB introducidos por el usuario
   bytes = mbytes * 1000000 # Se hace la conversión a bytes y se guarda en la variable bytes
   print(mbytes, "MB son", bytes, "bytes") # Se muestra al usuario el resultado

if __name__ == "__main__":
    main()