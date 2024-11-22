# Fungsi untuk menulis biodata ke dalam file
def tulis_biodata():
    # Membuka file Biodata.txt untuk menulis
    with open("Biodata.txt", "w") as file:
        # Mengambil input dari pengguna
        nama = input("Nama: ")
        umur = input("Umur: ")
        alamat = input("Alamat: ")
        email = input("Email: ")
        dosen_wali = input("Dosen Wali: ")

        # Menulis informasi ke dalam file
        file.write("Nama: " + nama + "\n")
        file.write("Umur: " + umur + "\n")
        file.write("Alamat: " + alamat + "\n")
        file.write("Email: " + email + "\n")
        file.write("Dosen Wali: " + dosen_wali + "\n")

    print("Biodata telah berhasil disimpan dalam Biodata.txt")

# Fungsi untuk membaca dan menampilkan biodata dari file
def baca_biodata():
    try:
        # Membuka file Biodata.txt untuk membaca
        with open("Biodata.txt", "r") as file:
            # Membaca dan menampilkan konten file
            print("\nBiodata yang disimpan:")
            print(file.read())
    except FileNotFoundError:
        print("File Biodata.txt tidak ditemukan. Pastikan file sudah ada.")

# Menjalankan fungsi untuk menulis dan membaca
tulis_biodata()  # Menulis biodata ke file
baca_biodata()   # Membaca dan menampilkan biodata dari file
