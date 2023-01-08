from Model.daftar_nilai import *
from View.view_nilai import *

#Mulai
print("===============================================================")
print("|                           Program 1                         |")
print("|    312210056                                     TI.22.C1   |")
print("|                        Sutan Krisno Adi                     |")
print("===============================================================")

while True:
    print("\n")
    menu = input("(L) Lihat, (T) Tambah, (H) Hapus, (U) Ubah, (C) Cari, (K) Keluar\nPilih menu: ")
    print("\n")

    # menu
    if menu.lower() == 't':
        tambah_data()

    elif menu.lower() == 'c':
        cari_data()

    elif menu.lower() == 'l':
        lihat_data()

    elif menu.lower() == 'u':
        ubah_data()

    elif menu.lower() == 'h':
        hapus_data()

    # Keluar
    elif menu.lower() == 'k':
        break

    else:
        print("Ada yang salah cuyy, silahkan cek kembali.")