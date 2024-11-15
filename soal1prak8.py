def penjumlahan_rekursif(angka_list, index=0):
    if index == len(angka_list):
        return 0
    else:
        return angka_list[index] + penjumlahan_rekursif(angka_list, index + 1)

jumlah = int(input("Masukkan Jumlah: "))
angka_list = []

for i in range(jumlah):
    angka = int(input(f"Masukkan angka ke-{i+1}: "))
    angka_list.append(angka)

hasil = penjumlahan_rekursif(angka_list)
print("Hasil dari penjumlahan adalah:", hasil)
