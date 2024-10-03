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
        jumlah = int(row['Jumlah'])
        bulan = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").strftime('%B')
        for _ in range(jumlah): 
            arr.append((ukuran, merk, warna, bulan))
    return arr
# Fungsi untuk mengurutkan kombinasi atribut menggunakan divide and conquer
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
            
# Fungsi untuk menggabungkan dua dictionary frekuensi
def mergeFreq(freq1, freq2):
    for key in freq2:
        if key in freq1:
            freq1[key] += freq2[key]
        else:
            freq1[key] = freq2[key]
    return freq1
# Fungsi untuk menghitung frekuensi atribut
def divideConquerFreq(arr, low, high):
    if low == high:
        ukuran_freq = {arr[low][0]: 1}
        merk_freq = {arr[low][1]: 1}
        warna_freq = {arr[low][2]: 1}
        bulan_freq = {arr[low][3]: 1}
        return ukuran_freq, merk_freq, warna_freq, bulan_freq
    else:
        mid = (low + high) // 2
        left_ukuran_freq, left_merk_freq, left_warna_freq, left_bulan_freq = divideConquerFreq(arr, low, mid)
        right_ukuran_freq, right_merk_freq, right_warna_freq, right_bulan_freq = divideConquerFreq(arr, mid + 1, high)

        ukuran_freq = mergeFreq(left_ukuran_freq, right_ukuran_freq)
        merk_freq = mergeFreq(left_merk_freq, right_merk_freq)
        warna_freq = mergeFreq(left_warna_freq, right_warna_freq)
        bulan_freq = mergeFreq(left_bulan_freq, right_bulan_freq)
        return ukuran_freq, merk_freq, warna_freq, bulan_freq
# Fungsi utama untuk menghitung dan mengurutkan kombinasi atribut
def frekUkuran(arr): 
    freq = {}
    divideConquer(arr, 0, len(arr) - 1, freq)
    freq_list = [(k, v) for k, v in freq.items()]
    ukuran_freq, merk_freq, warna_freq, bulan_freq = divideConquerFreq(arr, 0, len(arr) - 1)
    divideConquerSort(freq_list, ukuran_freq, merk_freq, warna_freq, bulan_freq)
    print("Kombinasi atribut sepatu dari yang paling populer:")
    for (ukuran, merk, warna, bulan), f in freq_list:
        print(f"Ukuran {ukuran}, Merk {merk}, Warna {warna}, Bulan {bulan}, muncul {f} kali")
# Cetak frekuensi atribut secara terpisah
def outputFrekAtributSepatu(arr):
    ukuran_freq, merk_freq, warna_freq, bulan_freq = divideConquerFreq(arr, 0, len(arr) - 1)
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
print("========== Solusi Parallel dengan Dataset Kecil ==========")     
file_path1 = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Kecil.csv'  #dataset-1
arr1 = baca_dari_csv(file_path1)
frekUkuran(arr1)
outputFrekAtributSepatu(arr1)

print("\n================================================\n")
print("========== Solusi Parallel dengan Dataset Sedang ==========") 
file_path2 = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Sedang.csv'  #dataset-2
arr2 = baca_dari_csv(file_path2)
frekUkuran(arr2)
outputFrekAtributSepatu(arr2)