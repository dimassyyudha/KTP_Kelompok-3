import pandas as pd
# Fungsi untuk membaca file CSV dan mengambil data yang dibutuhkan
def baca_dari_csv(file_path):
    data = pd.read_csv(file_path)
    arr = []
    for index, row in data.iterrows():
        ukuran = int(row['Ukuran'])
        jumlah = int(row['Jumlah'])
        for _ in range(jumlah):
            arr.append(ukuran)  
    return arr

# Divide and conquer untuk menghitung frekuensi ukuran
def divideConquer(arr, low, high, freq, min_val): 
    if arr[low] == arr[high]: 
        freq[arr[low] - min_val] += high - low + 1
    else: 
        mid = (low + high) // 2
        divideConquer(arr, low, mid, freq, min_val) 
        divideConquer(arr, mid + 1, high, freq, min_val) 
        
# Merge Sort untuk mengurutkan frekuensi ukuran
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        mergeSort(left_half)
        mergeSort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][1] > right_half[j][1]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        arr[k:] = left_half[i:] + right_half[j:]

# Fungsi utama untuk menghitung frekuensi ukuran sepatu
def frekUkuran(arr): 
    min_val = min(arr)
    max_val = max(arr)
    freq = [0] * (max_val - min_val + 1)
    divideConquer(arr, 0, len(arr) - 1, freq, min_val)
    freq_list = [(i + min_val, count) for i, count in enumerate(freq) if count > 0]
    mergeSort(freq_list)
    for elem, f in freq_list:
        print(f"Ukuran {elem} muncul {f} kali")

file_path = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Kecil.csv'  #dataset-1
#file_path = '../KTP_Kelompok-6/dataset/Dataset Penjualan Toko Sepatu - Sedang.csv'  #dataset-2
arr = baca_dari_csv(file_path)
frekUkuran(arr)

