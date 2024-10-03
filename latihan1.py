import math
a = float(input("Masukkan bilangan bulat a: "))
b = float(input("Masukkan bilangan bulat b: "))
# Menghitung hasil perhitungan
jumlah = a + b
selisih = b - a
kali = a * b
sisa_pembagian = a % b
pembagian = a / b
log_a = math.log10(a)
pangkat = a ** b
# Menampilkan hasil
print(f"Jumlah a dan b: {jumlah}")
print(f"Selisih b dan a: {selisih}")
print(f"Hasil kali a dan b: {kali}")
print(f"Sisa pembagian a dengan b: {sisa_pembagian}")
print(f"Pembagian a dengan b: {pembagian}")
print(f"Hasil dari log(a): {log_a}")
print(f"a pangkat b: {pangkat}")

