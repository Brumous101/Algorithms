# xn + 1 = xn * (xn * xn + 3 * A) / (3 * xn * xn + A)
def final(A,x1):
    xn1 = x1 + 1
    xn = x1
    output1 = 0
    #output2 = -1
    #i = 0
    while(xn != xn1):
        xn1 = xn * (xn * xn + 3 * A) / (3 * xn * xn + A)
        print(xn)
        print(xn1)
        #i = i + 1
        print()
    #while(i < 10):
    #    output1 = xn * (xn * xn + 3 * A) / (3 * xn * xn + A)
    #    print(output1)
    #    output2 = xn1 * (xn * xn + 3 * A) / (3 * xn * xn + A)
    #    print(output2)
    #    i = i + 1
    #    print()
    #while(output1 != output2):
    #    output1 = xn * (xn * xn + 3 * A) / (3 * xn * xn + A)
    #    print(output1)
    #    output2 = xn1 * (xn * xn + 3 * A) / (3 * xn * xn + A)
    #    print(output2)
    #    print()

final(99,900)