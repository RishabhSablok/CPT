def mean():
    repeat = True
    kka = True
    counter = 0
    total = 0
    while repeat:
        kka = True
        counter = 0
        total = 0
        while kka:
            a = input("Input the numbers here (Enter a string to stop): ")
            try:
                a = float(a)
                total += a
                counter += 1
            except:
                kka = False
                print(total/counter)
                print("Do you want to do it again?: ", end = "")
                repeat=("y" or "yes")in input().lower()

