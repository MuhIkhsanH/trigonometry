import math

def hitung_sudut(dasar, tinggi):
    # Hitung sudut menggunakan fungsi arctan
    sudut_radian = math.atan(tinggi / dasar)
    
    # Konversi sudut ke derajat
    sudut_derajat = math.degrees(sudut_radian)
    
    return sudut_derajat

# Panjang dua sisi
panjang_dasar = 40  # Dalam cm
tinggi = 26  # Dalam cm

# Hitung sudut menggunakan fungsi
hasil_hitung_sudut = hitung_sudut(panjang_dasar, tinggi)

# Output hasil
print(f"Sudut dalam segitiga tersebut adalah {hasil_hitung_sudut:.2f} derajat")
