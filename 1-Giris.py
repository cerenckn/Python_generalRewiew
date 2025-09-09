# -*- coding: utf-8 -*-
"""
Created on Mon Aug 25 11:22:37 2025

@author: crnck
"""

#%%   hücrelere ayırma


print("Python Eğitimi")
print("Python" + "Eğitimi")
print("Python" + " "+" Eğitimi") #boşlukta bir karakter

print ("İstanbul İzmir Ankara")  #kaçış karakteri \n
print ("İstanbul\nİzmir\nAnkara")

#print("Dünyanın en güzel yeri "Ankara'dır"")
print("Dünyanın en güzel yeri \"Ankara'dır\"")

print(r"C:/Users:/crnck") #row string= işlenmemiş string 

print("Python")
print("Eğitimi")

print("Python", end=" ")
print("Eğitimi")

print("Ceren","Çeken","2004",sep="-") #seperator 
print(2,3,2025, sep="/")
print("T","C",sep=".") #bunun yerine aşağıdaki komutta kullanılabilir
print(*"TC",sep=".")

print("Adı: Ceren "
      "Soyadı:Çeken "
      "D.Tarihi: 20.09.2004 ")

print("Adı:{} Soyadı:{} D.Tarihi:{}".format("Ceren","Çeken","20.09.2004"))

#TODO -> görev bölmelerine ayırıp daha sonra source -show todo listden bölmeleri görebiliriz


girdi=input("Lütfen bir sayı giriniz:")
print("Girdiğiniz sayı:",girdi)











