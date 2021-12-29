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

input = int(input("PROGRAM MENCARI NILAI FAKTORIAL DARI SEBUAH ANGKA\nMasukkan angka: "))
print("Nilai faktorialnya adalah:", faktorial(input))
