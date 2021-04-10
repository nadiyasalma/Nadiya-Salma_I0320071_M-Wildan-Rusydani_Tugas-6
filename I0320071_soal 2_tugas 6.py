#soal nomer 2

n = int(input("jumlah data :"))
nilai = []
angka = 0

for i in range(0,n):
    j = int(input("masukkan data ke-%d:" %(i+1)))
    nilai.append(j)
    angka += nilai[i]
    rata_rata = angka / n
print("Nilai rata-rata Anda adalah %0.2f" %rata_rata)