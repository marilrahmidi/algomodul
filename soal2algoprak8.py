def pangkat_rekursif(angka, pangkat):
    if pangkat == 0: 
        return 1
    elif pangkat > 0:  
        return angka ** pangkat
    else:  
        return 1 / pangkat_rekursif(angka, -pangkat)

angka = input("Angka: ")
if angka == '':
    print("bye") 
else:
    angka = float(angka)
    pangkat = int(input("Pangkat: "))
    hasil = pangkat_rekursif(angka, pangkat)
    print(hasil)
