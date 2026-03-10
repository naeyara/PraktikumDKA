import numpy as np
n = int(input("Jumlah Mahasiswa: "))

dtype_mhs = np.dtype([
    ('Nama', 'U50'), ('Nim', 'U10'), ('Nilai', 'f4'), ('TahunMasuk', 'i4')
])

data_mhs = np.zeros(n, dtype =dtype_mhs)

for i in range(n):
    print(f"\nData Mahasiswa ke-{i+1}")
    nama = input("Nama: ")
    nim = input("Nim: ")
    nilai = float(input("Nilai: "))
    tahun = int(input("Tahun Masuk: "))

    data_mhs[i] = (nama, nim, nilai, tahun)

print("\nData Mahasiswa: ")
for mhs in data_mhs:
    print(mhs)

nilai = data_mhs['Nilai']

print("\nNilai Mahasiswa: ")
print("Nilai Tertinggi: ", np.max(nilai))
print("Nilai Terendah: ", np.min(nilai))
print("Nilai Rata-rata: ", np.mean(nilai))

cari = input("\nMasukkan NIM atau Nama yang ingin dicari: ")
hasil = data_mhs[(data_mhs['Nim'] == cari) | (data_mhs['Nama'] == cari)]
if len(hasil) > 0:
    print("\nData ditemukan")
    for mhs in hasil:
        print(mhs)
else:
    print("Data tidak ditemukan")