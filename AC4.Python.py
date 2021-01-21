LINES = 7
def main():
    x = 1
    aux = 0
    count = 2
    for i in range(LINES):
        aux = x
        for j in range (LINES-aux):
            print(" ", end=" ")
        for k in range(x):
            print(aux, end=" ")
            aux-=1
        if x != 1:
            for h in range(x-1):
                print(count, end=" ")
                count+=1
        x+=1
        count=2
        aux-=1
        print()
    x = 6
    aux = 0
    count = 2
    for i in range(LINES-1):
        aux = x
        for j in range (LINES-aux):
            print(" ", end=" ")
        for k in range(x):
            print(aux, end=" ")
            aux-=1
        for h in range(x-1):
            print(count, end=" ")
            count+=1
        print()
        x-=1
        count=2
        aux-=1

if __name__ == "__main__":
    main()