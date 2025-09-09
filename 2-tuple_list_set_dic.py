# -*- coding: utf-8 -*-
isim = "Fatih"
print(isim == "Fatih")
print(isim == "FATİH")
print(isim != "Fatih")
print(isim == "KAAN")

# < sözlükte stringin önce gelmesi
# > sözlükte stringin sonra gelmesi
print("....")
print("a" > "B")  # true verdi.ASCII TABLOSUNDAN KAYNAKLI
print("A" > "B")  # false
print(ord("a"))  # 97
print(ord("A"))  # 65
print(ord("B"))  # 66

kelime1 = "ahmet"
kelime2 = "Mehmet"
print(kelime1 < kelime2)

kelime1 = kelime1.lower()
kelime2 = kelime2.lower()
print(kelime1, kelime2)
print(kelime1 < kelime2)


#NoneType 
sehir= None
print(type(sehir))

sehir= "Ankara"
print(type(sehir))

#Numeric: int, float, bool, compex sayilar
#complex()
#tuple immutable=değiştirilemez. 
'''
read-only sadece okunabilir özelliği var, bu da verilerin başkaları tarafından değiştirilmesini engeller.
verilerin korunumu için kullanılabşkir.
elemanların sequence number=sıra numarsı
tuple()
'''
tup1=(15,26,17,25)
tup2=("ahmet","mehmet")
tup3=(5+4j,"Melih",74.8,159)

#tup1[0]=174

tup1=(15,26,17,25)
tup2=("ahmet","mehmet")
tup3=(5+4j,"Melih",74.8,159)
tup4=tuple([79,125,14.69])

#tup1[0]=174  typeError veriyor, doğrudan değiştirelemiyor
butunTupler= tup1 + tup2 + tup3 + tup4

tup6=(15,26,17,25)
list1= [1,7,9,3,8]

print(tup6[1:])
print(list1[2:4])
print(tup6[0:len(tup6):2])

print(tup6.count(26))#count içine aldığı değerin kaç defa olduğuınu söyler


#number system conversion
#Binary
print(bin(2))
print(bin(19))
#Decimal
print(10)
print(10152)
#Octal
print(oct(26))
print(oct(65))
#hexadecimal
print(hex(17))

#LİST  VERİ TİPİ
'''
mutable=değiştirilebilir, doğrudan değiştirebiliriz
elemanlarına sequence number vardır
list()  []
'''
liste1=list([1,5,7,9])
liste2=[6,4,9,7,10,-5]

print(liste1)
liste1[3]=100
print(liste1)
print(liste1[-len(liste1)])

#Listelerde ekleme, güncelleme, silme

isimler=['Fatih','Kaan','Gül','Manolya']
isimler=isimler+["Ahmet","Mehmet"]
print(isimler)

isimler[0]="Ceren"
print(isimler)

isimler[1:4]= ["Selim" , "Oya" , "Zehra"]
print(isimler)

#isimler[1:4]= ["Selim","Oya","Zehra"]
#print(isimler)
# harf harf ekliyor!!!!!!!!!! isim isim ekleme gerekiyor


del isimler[5]
print(isimler)

isimler= isimler[:1] + isimler[3:]
print(isimler) 

#Liste Metotları
isimler=['Fatih','Kaan','Gül','Manolya']
yaslar=[28,35,44,58]

karısıkListe= isimler + yaslar
karısıkListe.extend({14.7,"selma",None,True,57})
karısıkListe+=[True,False,9+7j,"Naber"]

#print(karısıkListe.index("Deneme"))#---ValueError: içinde olmadığı için
print(karısıkListe.index("Naber"))
karısıkListe.append(175)
karısıkListe.insert(2, 14566)
print(karısıkListe)

karısıkListe.pop(7)
karısıkListe.extend([100,100,100])
karısıkListe.remove(100)#ilk karşılaştığını siliyor
karısıkListe.reverse()#tersine çeviriyor

liste= [2,5,7]
print(liste)
liste.reverse()
print(liste)

liste +=[-5,8,4,3,10,-9]
liste.sort()
print(liste)

print(isimler)
isimler.sort()
print(isimler)

#Çok boyutlu listeler
 
bilgiler=[["kaan",35],["ceren",21],["tolga",25]]
print(bilgiler[1])
print(bilgiler[0][1])

#bu listlerin içinde tuple şeklinde yazabiliriz ({}) bu şekilde,

bilgiler=[({185:"Fatih"}),("İstanbul","Denizli")]
bilgiler=[({185:"Fatih"},{192:"Melek"}),("İstanbul","Denizli")]
print(bilgiler[0])#bu bana sözlüğü veriyor böyle

#print(bilgiler[0][185])#bu bana keye karşılık gelen value gösteriyor
#yukarıdaki hata verir artık çünkü 0. indexe ulaştığımızda iki tane sözlük var

print(bilgiler[0][0][185])#bu şekilde yazarsak hata vermez
print(bilgiler[1][0])
print(bilgiler[1][1])

#SET(BENZERSİZ) VERİ TİPİ
'''
Mutable= değiştirilebilir
elemanların sequence number=sıra numarası yoktur
içeriisinde aynı değerde elemanlar barındırıamaz
{}
tc kimlik no gibi düşünebilşriz
arka planda 'hash' kullanıyor
index mantığı yok
'''
set1={5,12,2,6}
print(set1)
#set1.remove(100)#keyError 
set1.remove(12)
print(set1)

set2=set([5,4,7,8,9,4,7])
print(set2)#birden fazla aynı değeri almaz
 
set3= {4,1,8,9,-5,0,91}
print(set3)

set3.add(150)
print(set3)
set1.clear()
print(set1)#set()---set,boş 

set1.update({4,1,8,9,-5,0,91})
print(set1)

set1.pop()
print(set1)
set1.remove(-5)
print(set1)


set1={4,1,8,8,9-5,0,91,"Kaan","Selim"}
set2={3,4,8,7,-6,14,51,66,78,"Melek","Kaan"}
set3={3,4,8}
set4={100,200,300}


set5=set1.copy()#bir şey silerken kopyasından silinmez aynı anda
#ama set5=set1 yaptığımızda set1den silmek istediğimiz set5ten de silinir çünkü bu ikisi aynı obje
print(set1)
print(set5)
set1.remove(8)
print(set1)
print(set5)

print(set1.difference(set2))

set1.difference_update(set2)#=
set1=set1.difference(set2)
print(set1)#set1 set2 den farklı olanlara güncelledi kendini

print(set1.discard(150))#eleman yoksa NONE döndürüyor
set1.discard(0)#varsa siliyor
print(set1)#91,0 silinmiş durumda

print(set1.intersection(set2))#iki set arrasındaki kesişimi vrir
set1.intersection_update(set2)#set1 kesişime eştliyor
print(set1)

print(set3.isdisjoint(set4))#kesişimi boş kume mi diye bool değer döndürüyor
print(set4.issubset(set2))#altküme mi, subset=kapsayan küme mi demek

print(set5)
set5.pop()#keyfi olarak değer siler
print(set5)

#symetric_difference A-B-ANB
#union AUB

#DİCTİONARY=SÖZLÜK VERİ TİPİ
'''
mutable=değiştirilebilir
elemanların sequence number=sıra numarasu yerine key- value ilişkisi vardır
{}
dict()
'''

sozluk={1:"Fatih",2:"Kaan",3:"Aliye"}
set1={"Fatih","Aliye","Kaan"}

print(sozluk[3])#olmayan key istersek keyError hatası döndürüyor
print(sozluk.get(2))
print(sozluk.get(5,"Bu değerde kayıt yoktur"))

bosSozluk1={}
bosSozluk2=dict()

#sozluk2=dict([[1,2,3], ["A","B","C"]]) direkt böyle kendsisi eşleştirme yapamıyor
sozluk2=dict([(1,"A"),(2,"B"),(3,"C")])#bu şekilde elle ya da zipleyip yapacağız
anahtarlar=[1,2,3]
degerler=["A","B","C"]
sozluk2Elemanlari=zip(anahtarlar,degerler)
print(*sozluk2Elemanlari)

sozluk2Elemanlari=zip(anahtarlar,degerler)
sozluk=dict(sozluk2Elemanlari)
print(sozluk)

#ekleme,silme, güncelleme
keys=("Fatih","Kaan","Aliye")
values=['Bilgisayar müho','öğretmen','doktor']

sozlukElemanları=zip(keys,values)

bilgiler_meslek=dict(sozlukElemanları)
print(bilgiler_meslek)

print(bilgiler_meslek["Aliye"])
#ekleme, yoksa ekliyor otomatik
bilgiler_meslek["Mehmet"]="Makine müho"
print(bilgiler_meslek)
#varsa güncelliyor
bilgiler_meslek["Fatih"]="Makine müho"
print(bilgiler_meslek)
#silme del ile siliyotuz
del bilgiler_meslek["Mehmet"]
print(bilgiler_meslek)

#SÖZLÜK METOTLARI 

ogrencilerDers={'Okan':'Makine Öğrenmesi',
                'Ceren':'NLP',
                'Tolga':[{'Ders Adı':'Veri Tabanı','Hoca':'Gülşah'},
                         {'Ders Adı':'NLP','Hoca':'Burak'}]}


print(ogrencilerDers["Ceren"])
print(ogrencilerDers["Tolga"][0])
print(ogrencilerDers["Tolga"][1]['Hoca'])


baskaSozluk=ogrencilerDers.copy()#gölgesini kopyalıyor. birind eyapılan değişiklik diğreini etkilemez
baskaSozluk['Okan']='Mat1'
print(baskaSozluk)
print(ogrencilerDers)
sozluk1=dict.fromkeys(["Ali","Ceren","Burak"],0)
print(sozluk1)

print(ogrencilerDers.get('Okan'))
print(sozluk1.get('Okan','Bu anahtara ait değer yoktur!'))


print("dictionary: ",ogrencilerDers.items())
print("keys: ",ogrencilerDers.keys())
print("Values: ",ogrencilerDers.values())

ogrencilerDers.pop("Ceren")#belirtilen değeri atar
ogrencilerDers.popitem()#LIFO ya göre çıkarır

ogrencilerDers={'Okan':'Makine Öğrenmesi',
                'Ceren':'NLP',
                'Tolga':[{'Ders Adı':'Veri Tabanı','Hoca':'Gülşah'},
                         {'Ders Adı':'NLP','Hoca':'Burak'}]}

ogrencilerDers.setdefault('Okan','Ders Almadı')
ogrencilerDers.setdefault('Kemal','Ders Almadı')
sozluk2={'Ahmet':'Bilg 1'}
ogrencilerDers.update(sozluk2)#sozluk2 yi ogrencilerDersin içine ekliyor
print(ogrencilerDers)
sozluk3={"Levent":'Algebra'}
#ogrencilerDers+=sozluk3  Hata veriyor, dict lerde toplama operatörü yok
ogrencilerDers.update(sozluk3)#sozluk3 yi ogrencilerDersin içine ekliyor
print(ogrencilerDers)

































