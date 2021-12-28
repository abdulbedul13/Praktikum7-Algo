# -*- coding: utf-8 -*-
"""
Created on Tue Dec 28 19:57:12 2021
@author: Abdullah
"""


# ELEMEN KOMPETENSI 1
def faktorial(angka):
    faktor = 1
    for i in range(1, angka + 1):
        faktor *= i
    return faktor


elkom1 = int(input("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA\nMasukkan angka: "))
print("Nilai faktorialnya adalah:", faktorial(elkom1))

# ELEMEN KOMPETENSI 2
daftar_vokal = ["a", "i", "u", "e", "o"]

print("PROGRAM MENGHITUNG HURUF VOKAL DAN KONSONAN DARI KALIMAT")

elkom2 = str(input("Masukkan kalimat: ")).lower()

vokal = 0
konsonan = 0


def hitung(masuk):
    global vokal, konsonan
    for huruf in masuk:
        if huruf in daftar_vokal:
            vokal += 1
        else:
            konsonan += 1


hitung(elkom2)

print("Jumlah huruf vokal adalah ", vokal)
print("Jumlah huruf konsonan adalah ", konsonan)

# ELEMEN KOMPETENSI 3
print("PROGRAM PENGECEKAN BILANGAN")

while True:
    elkom3 = input("Masukkan bilangan, kosongkan jika ingin keluar: ")

    if elkom3 == "":
        break


    def pangkatkan(angka):
        return angka ** 3


    def cek_modulo(angka):
        if angka % 3 == 0:
            return True
        else:
            return False


    hasil = cek_modulo(int(elkom3))

    if hasil is True:
        print("Hasil:", pangkatkan(int(elkom3)), "\n")
    else:
        print("Hasil:", hasil, "\n")
