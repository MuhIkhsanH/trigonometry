import math

def hitung_sudut_siku_siku(panjang_dasar, tinggi):
    # Memastikan segitiga siku-siku dengan sudut 90 derajat
    if panjang_dasar == tinggi:
        return 90.0
    else:
        return None

def hitung_sudut(dasar, tinggi):
    # Hitung sudut menggunakan fungsi arctan
    sudut_radian = math.atan(tinggi / dasar)
    
    # Konversi sudut ke derajat
    sudut_derajat = math.degrees(sudut_radian)
    
    return sudut_derajat

# Panjang dua sisi
panjang_dasar = 40  # Dalam cm
tinggi = 26  # Dalam cm

# Hitung sudut siku-siku
sudut_siku_siku = hitung_sudut_siku_siku(panjang_dasar, tinggi)

# Hitung sudut menggunakan fungsi arctan
hasil_hitung_sudut = hitung_sudut(panjang_dasar, tinggi)

# Output hasil
if sudut_siku_siku is not None:
    print(f"Sudut dalam segitiga tersebut adalah {sudut_siku_siku:.2f} derajat (segitiga siku-siku)")
else:
    print(f"Sudut dalam segitiga tersebut adalah {hasil_hitung_sudut:.2f} derajat (segitiga tidak siku-siku)")
