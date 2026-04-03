for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")

    elif i % 5 == 0:
        print("Buzz")
   
    else:
        print(i)
def konversi_hari():
    try:
        x = int(input("Masukkan jumlah hari: "))
        
        tahun = x // 365
        sisa_hari_setelah_tahun = x % 365
        
        bulan = sisa_hari_setelah_tahun // 30
        hari = sisa_hari_setelah_tahun % 30
        
        print(f"Hasil: {tahun} tahun, {bulan} bulan, {hari} hari")
    except ValueError:
        print("Mohon masukkan angka saja.")

if __name__ == "__main__":
    konversi_hari()