import pandas as pd

def frekuensiUkuran(arr, n): 
    mp = {} 
    for i in range(n): 
        ukuran = arr[i][0]
        jumlah = arr[i][1]
        
        if ukuran not in mp: 
            mp[ukuran] = 0
        mp[ukuran] += jumlah

    freq_list = [(key, value) for key, value in mp.items()]

    # Selection Sort untuk mengurutkan frekuensi
    for i in range(len(freq_list)):
        max_idx = i
        for j in range(i + 1, len(freq_list)):
            if freq_list[j][1] > freq_list[max_idx][1]:
                max_idx = j
        freq_list[i], freq_list[max_idx] = freq_list[max_idx], freq_list[i]

    for elem, f in freq_list:
        print("Sepatu ukuran", elem, "muncul", f, "kali") 

#Main 
file_path = '../tubes/lib/Dataset Penjualan Toko Sepatu - Sedang.csv' #dataset-1
#file_path = '../tubes/lib/Dataset Penjualan Toko Sepatu - Kecil.csv'  #dataset-2
data = pd.read_csv(file_path)
arr = data[['Ukuran', 'Jumlah']].values
n = len(arr)
frekuensiUkuran(arr, n)
