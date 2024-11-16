def ordinal_suffix(number):
    if 10 <= number % 100 <= 20:
        suffix = 'th'
    else:
        suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(number % 10, 'th')
    return f"({number}, '{suffix}')"

print("Ordinal Number")
print("Ketik 0 untuk menghentikan program")

while True:
    try:
        number = int(input("Masukkan angka: "))
        if number == 0:
            print("Terima kasih telah menggunakan program saya")
            break
        print(ordinal_suffix(number))
    except ValueError:
        print("Masukkan angka yang valid.")
