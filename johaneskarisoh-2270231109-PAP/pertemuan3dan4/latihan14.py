data="ini adalah string"
print(data)
print(type(data))

#1.cara membuat string
#1,dengan menggunakan single quote'...'
#2.dengan menggunakan double quote"..."

data='menggunakan singgle quote'
print(data)
data="menggunakan doble quote"
print(data)
print("Halo,apa kabar?")
print("Halo,apa kabar?")
print("ini adalah hari jum\'at")

#2.menggunakan tanda \
#membuat tanda ' menjadi string
print('mari shalat jum\'at')
print('g\'day,isn\'t it?')

#blacklash
print("C:\\user\\Ucup")
#tab
print("ucup\t\totong,semakin jauhan")
#backspace
print("ucup\botong,jadi deketan")
#newline
print("baris pertama.\nbaris kedua") #LF->line feed->unix,macos,linux
print("baris pertama.\nbarus kedua.") #CR-> carriafe return->commodore,corn,lisp
print("baris pertama.\r\nbaris kedua.") #CRLF->line feed carriage return->dipakai oleh windows

#3,string literal atau raw
#hati-hati
print('C:\new folder')#akan salah pathnya
#menggunakan raw string
print(r'C:\new folder')
#multiline literal sting
print(""" 
Nama: Ucup
Kelas: 3 SD 
""")

#multiline literal string dan RAW
print(r"""
Nama:Ucup
Kelas:3 SD\new normal
Website:www.ucup.com/newID
""")





















