def konversi_nilai_mutu(kategori_nilai, nilai_default=0.0):
    """
    Mengkonversi kategori huruf menjadi Nilai Mutu numerik (IP).

    Args:
        kategori_nilai (str): Kategori nilai huruf (A, B, C, D, E).
        nilai_default (float, optional): Nilai yang dikembalikan jika kategori tidak valid. Default 0.0.

    Returns:
        float: Nilai Mutu numerik.
    """
    kategori_nilai = kategori_nilai.upper() 
    
    # Mapping Nilai Mutu/IP
    nilai_mutu_mapping = {
        'A': 4.0,
        'B': 3.0,
        'C': 2.0,
        'D': 1.0,
        'E': 0.0
    }

    # Menggunakan nilai_default jika kategori_nilai tidak ditemukan
    # Ini adalah implementasi dari argumen default/parameter
    return nilai_mutu_mapping.get(kategori_nilai, nilai_default)

# --- Bagian Utama Program ---
def hitung_rata_rata():
    """
    Mengumpulkan input kategori nilai dari pengguna dan menghitung rata-rata Nilai Mutu.
    """
    list_nilai_mutu = []
    
    print("Masukkan kategori nilai huruf (A, B, C, D, E).")
    print("Tekan ENTER/kosongkan input untuk mengakhiri dan menghitung rata-rata.")
    
    while True:
        # Input pengguna
        input_kategori = input("masukkan nilai: ").strip()
        
        # Cek kondisi berhenti
        if not input_kategori:
            break
            
        # Panggil fungsi untuk konversi dan mendapatkan nilai_mutu (menggunakan pengembalian nilai)
        nilai_mutu = konversi_nilai_mutu(input_kategori)
        
        # Tampilkan Nilai Mutu yang dikonversi
        print(f"nilai = {nilai_mutu}")
        
        # Tambahkan nilai_mutu ke daftar jika valid (nilai > 0.0, atau jika kita ingin memasukkan 'E' yang bernilai 0.0)
        # Jika nilai_mutu adalah 0.0, itu bisa jadi 'E' atau input tidak valid
        # Kita akan berasumsi semua input yang dikonversi (termasuk 'E') dihitung
        if input_kategori.upper() in ['A', 'B', 'C', 'D', 'E']:
             list_nilai_mutu.append(nilai_mutu)
        else:
            print("Kategori nilai tidak valid. Nilai dihitung sebagai 0.0.")


    # Perhitungan Rata-rata
    if list_nilai_mutu:
        total_nilai = sum(list_nilai_mutu)
        jumlah_input = len(list_nilai_mutu)
        rata_rata = total_nilai / jumlah_input
        print(f"\nRata-ratanya adalah: {rata_rata:.1f}")
    else:
        print("\nTidak ada nilai yang valid dimasukkan.")

# Jalankan program
hitung_rata_rata()
