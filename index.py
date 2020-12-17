import os
import sys

def pindah(label):
    global nomor
    nomor = label

def clearscreen():
    os.system('cls')

def keluar():
    sys.exit()

def ulang():
    ulang = input("Apakah anda ingin mengulang  lagi ? [y/n] ")
    if ulang == "y" or ulang == "Y" :
        pindah(0)
        clearscreen()
    elif ulang == "n" or ulang == "N" :
        clearscreen()
        keluar()
    else :
        keluar()
        
def rumus():
    global harga, berat, total, jenisn
    
    total = berat * harga

def cetak():
    print ("")
    print( "=========================================")
    print( "|         Aplikasi Bank Sampah          |")
    print ("=========================================")
    print( "| Nama Sampah        : ", nama)
    print ("| Jenis Sampah         : ", jenisn)
    print ("| Berat Sampah     : " , berat, " kg")
    print ("| Kondisi Sampah  : ", kond)
    
    print ("")
    print ("=> Total Harga : Rp. ", total)
    print ("")

nomor = 0

while True :

    if nomor == 0 :
        clearscreen()
        print( "--------------------")
        print( "Aplikasi Bank Sampah")
        print( "--------------------")
        print( "" )
        print( "Jenis Sampah   |  Kondisi Sampah" )
        print( "1. Plastik     |  1. Bersih     " )
        print( "2. Kertas      |  2. Bekas      " )
        print( "3. Besi        |  3. Kotor      " )
        print( "4. Kaca        |  4. Rusak      " )
        print( "" )
        nama = input("Masukkan Nama Sampah : ")
        jenis = int(input("Jenis Sampah (1/2/3/4) : "))
        berat = int(input("Masukkan Berat Sampah (kg) : "))
        kond = int(input("Kondisi Sampah : "))
        
        if jenis == 1 :
            pindah(1)
        elif jenis == 2 :
            pindah(2)
        elif jenis == 3 :
            pindah(3)
        elif jenis == 4 :
            pindah(4)
        else :
            pindah(0)

    elif nomor == 1 :
        jenisn = "Plastik"
        harga = 2000
        
        clearscreen()
        rumus()
        cetak()
        ulang()

    elif nomor == 2 :
        jenisn = "Kertas"
        harga = 4000
        
        clearscreen()
        rumus()
        cetak()
        ulang()

    elif nomor == 3 :
        jenisn = "Besi"
        harga = 10000
        
        clearscreen()
        rumus()
        cetak()
        ulang()

    elif nomor == 4 :
        jenisn = "Kaca"
        harga = 7000
        
        clearscreen()
        rumus()
        cetak()
        ulang()
    else :
        keluar()
