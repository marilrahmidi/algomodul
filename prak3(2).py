import math
def hitung_determinan(a, b, c):
    return b**2 - 4*a*c

def jenis_akar(diskriminan):
    if diskriminan > 0:
        return "Akar real dan berbeda."
    elif diskriminan == 0:
        return "Akar real dan sama."
    else:
        return "Akar kompleks."

def cari_akar(a, b, c, diskriminan):
    if diskriminan >= 0:
        akar1 = (-b + math.sqrt(diskriminan)) // (2*a)
        akar2 = (-b - math.sqrt(diskriminan)) // (2*a)
        if diskriminan == 0:
            return f"Akar: {akar1}"
        else:
            return f"Akar-akar: {akar1} dan {akar2}"
    else:
        akar_real = -b // (2*a)
        akar_imaginer = math.sqrt(abs(diskriminan)) // (2*a)
        return f"Akar kompleks: {akar_real} + {akar_imaginer} dan {akar_real} - {akar_imaginer}"

def tampilkan_persamaan(a, b, c):
    persamaan = f"{a}x² + {b}x + {c} = 0"
    return persamaan

a = int(input("Nilai a: "))
b = int(input("Nilai b: "))
c = int(input("Nilai c: "))

print("Persamaan kuadrat:", tampilkan_persamaan(a, b, c))

diskriminan = hitung_determinan(a, b, c)
print(f"Diskriminan: {diskriminan}")

print(jenis_akar(diskriminan))

hasil_akar = cari_akar(a, b, c, diskriminan)
print(hasil_akar)
