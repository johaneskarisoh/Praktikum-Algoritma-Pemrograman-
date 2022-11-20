#NAMA:JOHANES KARISOH
#NIM:2270231109

print('BENGKEL JAYA'.center(50))
print('JL.RAYA BEKASI KM:18'.center(50))
print("=================================================","\n")

print("DAFTAR PERAWATAN KENDARAAN:".center(50))
print("GANTI OLI      : Rp.150.000")
print("CEK REM        : Rp.50.000")
print("TUNE UP        : Rp.50.000")
print("SERVICE RINGAN : Rp.250.000")
print("SERVICE BESAR  : Rp.400.000")

print("--------------------------------------------------")

perbaikan={
    "GANTI OLI":150000,
    "CEK REM":50000,
    "TUNE UP":50000,
    "SERVICE KECIL":250000,
    "SERVICE BESAR":400000,
    
}

nama=input("NAMA PELANGGAN     :")
pilih=input("PILIH PERBAIKAN    :")
pilih2=input("PERBAIKAN TAMBAHAN\n cukup jika sudah  :")
alamat=input("ALAMAT             :")
telp=input("NO TELPON          :")

import datetime

waktu_sekarang=datetime.datetime.now()

print("-------------------------------------------------","\n")
print("BUKTI PEMBAYARAN".center(50),"\n")
print("NAMA PELANGGAN :",nama)
if pilih2=='CUKUP':
    print("PERBAIKAN      :",pilih)
elif pilih2=="CEK REM" or pilih2=="TUNE UP" or pilih2=="GANTI OLI":
    print("PERBAIKAN      :",pilih+ '-',pilih2)

print("ALAMAT         :",alamat)
print("NO TELPON      :",telp)
print("TANGGAL        :",waktu_sekarang)

if pilih2=="CUKUP":
    bayar=perbaikan[pilih]
    print("TOTAL BAYAR    :",bayar,"\n")
elif pilih2=="CEK REM" or pilih2=="TUNE UP" or pilih2=="GANTI OLI":
    bayar2=perbaikan[pilih]+perbaikan[pilih2]
    print("TOTAL BAYAR    :",bayar2,"\n")
print("TERIMA KASIH TELAH MENGGUNAKAN JASA KAMI".center(50),"\n")

