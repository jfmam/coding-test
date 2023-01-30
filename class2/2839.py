n = int(input())
a = n // 5
b = (n - (5*a)) // 3

if (5*a) + (b * 3) == n:
    print(a+b)
else:
    while a != 0:
        a -= 1
        b = (n - (5*a)) // 3
        if(5*a) + (b * 3) == n:
            print(a+b)
            exit()
    print(-1)
            
