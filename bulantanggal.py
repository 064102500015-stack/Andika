def is_tahun_kabisat(tahun):
    """Menentukan apakah suatu tahun adalah tahun kabisat."""
    # Tahun kabisat adalah tahun yang habis dibagi 4, 
    # kecuali jika habis dibagi 100 tetapi tidak habis dibagi 400.
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        return True
    else:
        return False

def hitung_jumlah_hari(bulan, tahun):
    """Menghitung jumlah hari dalam suatu bulan dan tahun."""
    
    # Bulan dengan 31 hari
    if bulan in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    # Bulan dengan 30 hari
    elif bulan in [4, 6, 9, 11]:
        return 30
    # Bulan Februari (bulan 2)
    elif bulan == 2:
        if is_tahun_kabisat(tahun):
            return 29
        else:
            return 28
    # Seharusnya tidak tercapai karena validasi input
    else:
        return 0 

# --- Input dan Validasi Menggunakan Perulangan WHILE ---

# 1. Validasi Input Bulan (1-12)
bulan = 0  # Inisialisasi variabel bulan
while not (1 <= bulan <= 12):
    try:
        bulan = int(input("Masukkan angka bulan (1-12): "))
        if not (1 <= bulan <= 12):
            print("❌ Input bulan tidak valid. Masukkan angka antara 1 sampai 12.")
    except ValueError:
        print("❌ Input tidak valid. Harap masukkan angka bulat untuk bulan.")
        bulan = 0 # Tetapkan kembali 0 agar perulangan berlanjut

# 2. Validasi Input Tahun (Positif)
tahun = 0 # Inisialisasi variabel tahun
while tahun <= 0:
    try:
        tahun = int(input("Masukkan tahun (contoh: 2024): "))
        if tahun <= 0:
            print(" Input tahun tidak valid. Masukkan angka tahun positif.")
    except ValueError:
        print(" Input tidak valid. Harap masukkan angka bulat untuk tahun.")
        tahun = 0 # Tetapkan kembali 0 agar perulangan berlanjut

# --- Pemrosesan dan Output ---

jumlah_hari = hitung_jumlah_hari(bulan, tahun)

# Daftar nama bulan untuk output yang lebih jelas
nama_bulan_list = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", 
                   "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
nama_bulan = nama_bulan_list[bulan - 1]

print("\n=============================================")
print(f"🗓️ Bulan yang Anda masukkan adalah: {nama_bulan} {tahun}")
print(f"    Jumlah hari dalam {nama_bulan} {tahun} adalah: {jumlah_hari} hari")
print("=============================================")