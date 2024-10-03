import pandas as pd
from datetime import datetime

# Fungsi untuk membaca file CSV dan mengambil data yang dibutuhkan
def baca_dari_csv(file_path):
    data = pd.read_csv(file_path)
    arr = []
    for index, row in data.iterrows():
        timestamp = row['Timestamp']
        ukuran = int(row['Ukuran'])
        merk = row['Merk Sepatu']
        warna = row['Warna']
        bulan = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime('%B')
        arr.append((ukuran, merk, warna, bulan))
    return arr

# Fungsi untuk menghitung frekuensi kombinasi atribut menggunakan divide and conquer
def divideConquer(arr, low, high, freq):
    if low == high:
        if arr[low] not in freq:
            freq[arr[low]] = 0
        freq[arr[low]] += 1
    else:
        mid = (low + high) // 2
        divideConquer(arr, low, mid, freq)
        divideConquer(arr, mid + 1, high, freq)

# Fungsi merge sort untuk mengurutkan kombinasi atribut berdasarkan frekuensi tiap sepatu
def divideConquerSort(freq_list, ukuran_freq, merk_freq, warna_freq, bulan_freq):
    if len(freq_list) > 1:
        mid = len(freq_list) // 2
        left_half = freq_list[:mid]
        right_half = freq_list[mid:]

        divideConquerSort(left_half, ukuran_freq, merk_freq, warna_freq, bulan_freq)
        divideConquerSort(right_half, ukuran_freq, merk_freq, warna_freq, bulan_freq)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            left_attr = left_half[i][0]
            right_attr = right_half[j][0]

            if (ukuran_freq[left_attr[0]], merk_freq[left_attr[1]], warna_freq[left_attr[2]], bulan_freq[left_attr[3]]) > \
               (ukuran_freq[right_attr[0]], merk_freq[right_attr[1]], warna_freq[right_attr[2]], bulan_freq[right_attr[3]]):
                freq_list[k] = left_half[i]
                i += 1
            else:
                freq_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            freq_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            freq_list[k] = right_half[j]
            j += 1
            k += 1

# Fungsi untuk menghitung frekuensi setiap atribut
def frekAtributSepatu(arr):
    ukuran_freq = {}
    merk_freq = {}
    warna_freq = {}
    bulan_freq = {}

    for ukuran, merk, warna, bulan in arr:
        if ukuran not in ukuran_freq:
            ukuran_freq[ukuran] = 0
        ukuran_freq[ukuran] += 1
        if merk not in merk_freq:
            merk_freq[merk] = 0
        merk_freq[merk] += 1
        if warna not in warna_freq:
            warna_freq[warna] = 0
        warna_freq[warna] += 1
        if bulan not in bulan_freq:
            bulan_freq[bulan] = 0
        bulan_freq[bulan] += 1

    return ukuran_freq, merk_freq, warna_freq, bulan_freq

# Fungsi utama untuk menghitung dan mengurutkan kombinasi atribut
def frekUkuran(arr): 
    freq = {}
    divideConquer(arr, 0, len(arr) - 1, freq)
    freq_list = [(k, v) for k, v in freq.items()]
    ukuran_freq, merk_freq, warna_freq, bulan_freq = frekAtributSepatu(arr)
    divideConquerSort(freq_list, ukuran_freq, merk_freq, warna_freq, bulan_freq)
    print("Kombinasi atribut sepatu dari yang paling populer:")
    for (ukuran, merk, warna, bulan), f in freq_list:
        print(f"Ukuran {ukuran}, Merk {merk}, Warna {warna}, Bulan {bulan} ")

# Cetak frekuensi atribut secara terpisah
def outputFrekAtributSepatu(arr):
    ukuran_freq, merk_freq, warna_freq, bulan_freq = frekAtributSepatu(arr)

    print("\nFrekuensi per atribut:")
    print("Ukuran:")
    for ukuran, f in ukuran_freq.items():
        print(f"Ukuran {ukuran} muncul {f} kali")
    print("\nMerk:")
    for merk, f in merk_freq.items():
        print(f"Merk {merk} muncul {f} kali")
    print("\nWarna:")
    for warna, f in warna_freq.items():
        print(f"Warna {warna} muncul {f} kali")
    print("\nBulan:")
    for bulan, f in bulan_freq.items():
        print(f"Bulan {bulan} muncul {f} kali")

#Main    
file_path = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Sedang.csv' #dataset-1
#file_path = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Kecil.csv'  #dataset-2
arr = baca_dari_csv(file_path)
frekUkuran(arr)
outputFrekAtributSepatu(arr)