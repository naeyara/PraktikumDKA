import numpy as np
n = int(input("Jumlah Barang: "))

dtype_brg = np.dtype([
    ('NamaBarang', 'U50'), ('KodeBarang', 'U10'), ('Jumlah', 'i4'), ('HargaPerUnit', 'f4')
])

data_brg = np.zeros(n, dtype =dtype_brg)

for i in range(n):
    print(f"\nData Barang ke-{i+1}")
    nama = input("Nama Barang: ")
    kode = input("Kode Barang: ")
    jumlah = float(input("Jumlah: "))
    harga = int(input("Harga Per Unit: "))

    data_brg[i] = (nama, kode, jumlah, harga)

print("\nData Barang: ")
for barang in data_brg:
    print(barang)

total = data_brg['Jumlah'] * data_brg['HargaPerUnit']

print("\nTotal Nilai Inventaris tiap barang: ")
for i in range(n):
    print(data_brg['NamaBarang'][i], '=', total[i])

cari = input("\nMasukkan Nama Barang atau Kode Barang yang ingin dicari: ")
hasil = data_brg[(data_brg['NamaBarang'] == cari) | (data_brg['KodeBarang'] == cari)]
if len(hasil) > 0:
    print("\nData ditemukan")
    for barang in hasil:
        print(barang)
else:
    print("Data tidak ditemukan")