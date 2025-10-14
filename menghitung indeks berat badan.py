nama = input("Masukan nama kamu: ")
TB = float(input("masukan tinggi badan kamu (dalam cm): "))
BB = float(input("masukan berat badan kamu (dalam kg) "))
tinggi = TB / 100

BMI = BB / (tinggi ** 2)

if BMI <18.5:
    kategori = "kurus"
elif 18.5 <= BMI <25:
    kategori = "normal"
elif 25 <= BMI < 30:
    kategori = "gemuk"
else:
    kategori = "obesitas" 

print (f"{nama}, skor BMI kamu adalah {BMI:.1f}. kategori : {kategori}")




