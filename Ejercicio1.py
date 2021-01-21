def main():
    sentence = input("Introduce la frase que quieres ver al reves: ")
    print("")
    firstchar= input("Cambia la primera letra de lo que has introducido: ")
    sentence_new= firstchar + sentence[1:]
    print("")
    print("Tu frase al reves es=", sentence_new[::-1])

if __name__ == "__main__":
    main()