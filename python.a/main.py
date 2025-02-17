
number=10
print(number)
name='ceyda'
print (name)
print(type(name))

name=20
print(type(name))

age=21 #atama opretarleri

print(25+20)
print(50-15)
print(100/20)#bu ondalıklı sayı verir tam sayı ısteren // kullan
print(50*2)
print(100%2)#kalani gosterir
print(5**2)#üs alma


is_active= True #boolean veri tipidir

#KARSILASTIRMA OPERATORLERi
print(1==1) #karsılasturma operatıru bool sekide cevap dondurur
print(1==2)
print(1!=2)
print(1<=2)

#MANTUKSAL OPERATORLER and or not
print("mantıksal: ")
print(1==1 and 10==10)
print(1==1 and 10==11)# and de ikisi de dogru olmalı yoksa false ılur
print("/////////////")
print(1==1 or 10==10)
print(1==1 or 10==11) #or da iki durumdan birin,n dogru olması yeterli
print("/////////////")
print(1==1 and 5==5 or 25<10 and 150<100)
print("*************")
print(not 1==1)# boyle degılse yap gibi

print("ATAmA OPERATORLERİ")
x=5

x+=3
#butun opertaorlerin atma opertaouyle yan yana calısma gibi bir özellıhı vardır
print(x)
x**=5
print(x)

#LİSTE
students=["beyza","ali","yusuf",5,True ] #python typr safe olmadıgı için aynı tipten omal zaorunsa degıldır

print(students)
students.append("edanur") # ekleme için fonktur
print(students)
students.pop()
print(students)
print(students[3])# 3.indeste 5 var 


a=5
b=a
b+=10
print (a)
print (b)

a_list=["eleman 1","eleman 2"]
#yapay zeka içn python ders1
