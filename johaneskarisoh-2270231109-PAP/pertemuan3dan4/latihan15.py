#Date and time(latihan)

import datetime as dt
print("silahkan masukan tanggal,\nbulan dan tahun lahir anda")
tanggal=int(input("tanggal \t:"))
bulan  =int(input("bulan \t\t:"))
tahun  =int(input("tahun \t\t:"))

tanggal_lahir=dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")
hari_ini=dt.date.today()
print(f"Hari ini tanggal          : {hari_ini}")
umur_hari=hari_ini-tanggal_lahir
umur_tahun=umur_hari.days//365
umur_bulan_sisa=(umur_hari.days%365)//30
print(f"Harinya adalah            : {tanggal_lahir:%A}")
print(f"Umur anda adalah          : {umur_tahun} tahun, {umur_bulan_sisa} bulan")
