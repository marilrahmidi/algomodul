# Meminta pengguna untuk memasukkan nilai input
n = int(input("Masukkan nilai: "))

# Menggunakan perulangan for untuk menghasilkan output
for i in range(n, 0, -1):
  print(str(i) * i)
