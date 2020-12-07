n = 1
def mccarthy(n):
    counter = 0
    while(n < 25):
        counter = counter + (n*n*n)
        print(counter)
        n=n +1
        print(n)

    return counter

print(mccarthy(1))