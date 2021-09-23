import math as m 
def main():
    marbel_count = 0
    x = 0.0
    y = 0.0
    p = 0.0
    q = 0.0
    z = 0.0

    test_case = int(input())

    for i in range(test_case):
        first = input()
        p, q, z = first.split(" ")
        p = float(p)
        q = float(q)
        z = float(z)

        g = (p)/2
        f = (q)/2
        radius = m.sqrt((g**2 + f**2 - z))
        #print(radius)
        n = int(input())
        
        for j in range(n):
            coord = input()
            x, y = coord.split(" ")
            x = int(x)
            y = int(y)

            

            if ( g-abs(x) )< radius:
                if ( f-abs(y) ) < radius:
                    marbel_count = marbel_count+1
    print(marbel_count)




if __name__ == "__main__":
    main()