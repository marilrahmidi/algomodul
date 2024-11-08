import math
x = False
n = ""

def not_prime(n):
    if n % 2 == 0 and n > 2: 
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        print(n, "bukanlah bilangan Prima")
    elif n == 1:
        print("bukanlah bilangan Prima")
    else:
        is_prime(n)

def is_prime(n):
    print(n, "adalah bilangan Prima")
    
while (not x):
    print("Gunakan 0 untuk stop")
    n = int(input("masukan angka: "))
    if n == 0:
        x = True
    else:
        not_prime(n)
