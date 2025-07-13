def quick_sort_siswa(data_siswa):
    """
    Mengurutkan daftar siswa berdasarkan nilai rata-rata menggunakan algoritma Quick Sort.
    """
    def _quick_sort(arr, low, high):
        if low < high:
            # pi adalah indeks partisi, arr[pi] sekarang berada di posisi yang benar
            pi = _partition(arr, low, high)

            # Urutkan secara rekursif elemen sebelum dan sesudah partisi
            _quick_sort(arr, low, pi - 1)
            _quick_sort(arr, pi + 1, high)

    def _partition(arr, low, high):
        # Pilih elemen paling kanan sebagai pivot (nilai rata-rata)
        pivot = arr[high]['nilai_rata_rata']

        # Indeks elemen yang lebih kecil
        i = low - 1

        for j in range(low, high):
            # Jika elemen saat ini lebih kecil dari atau sama dengan pivot
            if arr[j]['nilai_rata_rata'] <= pivot:
                i += 1
                # Tukar arr[i] dan arr[j]
                arr[i], arr[j] = arr[j], arr[i]

        # Tukar arr[i + 1] dan arr[high] (pivot)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Panggil fungsi rekursif Quick Sort
    _quick_sort(data_siswa, 0, len(data_siswa) - 1)
    return data_siswa

# Contoh penggunaan:
data_siswa = [
    {'nama': 'Budi', 'nilai_rata_rata': 85},
    {'nama': 'Ani', 'nilai_rata_rata': 92},
    {'nama': 'Joko', 'nilai_rata_rata': 78},
    {'nama': 'Siti', 'nilai_rata_rata': 95},
    {'nama': 'Rina', 'nilai_rata_rata': 88},
    {'nama': 'Dina', 'nilai_rata_rata': 85}, # Tambahan untuk melihat stabilisasi pada nilai yang sama
]

print("Data siswa sebelum diurutkan:")
for siswa in data_siswa:
    print(siswa)

data_terurut = quick_sort_siswa(data_siswa)

print("\nData siswa setelah diurutkan berdasarkan nilai rata-rata:")
for siswa in data_terurut:
    print(siswa)
