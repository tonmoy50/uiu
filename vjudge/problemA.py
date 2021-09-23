


def main():
    t = 0
    t = int(input())

    for i in range(t):
        input_vals = input()
        p, y, r1, r2 = input_vals.split(" ")
        p = float(p)
        y = float(y)
        r1 = float(r1)
        r2 = float(r2)

        bank1 = ( p * (1+ (r1/100)  )**y ) - p
        bank2 = p * y * ( r2/100)

        if bank1 < bank2:
            print("Bank 1")
        elif bank1 > bank2: 
            print("Bank 2")
        else: 
            print("Confused huh!")








if __name__ == "__main__":
    main()