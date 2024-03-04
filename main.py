sayi1 = int(input("İlk Sayıyı Giriniz : "))
sayi2 = int(input("İkinci Sayıyı Giriniz : "))

islem = input("Yapmak İstediğiniz İşlemi Seciniz!:"
         "(Toplama : + , Çıkarma : - , Çarpma : x , Bölme : / ) ")
print(islem)

if islem == "+":
    print("Sonuç: "+str(sayi1+sayi2))
elif islem == "-":
    print("Sonuç: "+str(sayi1-sayi2))
elif islem == "x":
    print("Sonuç: "+str(sayi1*sayi2))
elif islem == "/":
    print("Sonuç: "+str(sayi1/sayi2))

else:
    print("Geçersiz İşlem!")
