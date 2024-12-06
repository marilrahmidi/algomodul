class Mahasiswa:
    def __init__(self, nama, nim, jurusan, angkatan,):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.angkatan = angkatan

    def tampilkan_biodata(self):
        print("\n=== Biodata Mahasiswa ===")
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"angkatan  : {self.angkatan}")


def main():
    total_mahasiswa = 0
    nama = input("Masukkan nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan jurusan: ")
    angkatan = input("Masukkan angkatan: ")
    total_mahasiswa += 1

    mahasiswa = Mahasiswa(nama, nim, jurusan, angkatan)

    mahasiswa.tampilkan_biodata()
    print(f"\nTotal mahasiswa yang telah diinput: {total_mahasiswa}")



main()
