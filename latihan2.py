import math

lintang1 = math.radians(float(input("Lintang kota 1: ")))
bujur1 = math.radians(float(input("Bujur kota 1 : ")))
lintang2 = math.radians(float(input("Lintang kota 2 : ")))
bujur2 = math.radians(float(input("Bujur kota 2 : ")))
R = 6371
lintang = lintang2-lintang1
bujur = bujur2-bujur1
a = math.sin(lintang2/2)*2 + math.cos(lintang1)*math.cos(lintang2)*math.sin(bujur/2)*2
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a) )
d = R * c
print(f"Jarak antara dua titik tersebut adalah {d} kilometer")
