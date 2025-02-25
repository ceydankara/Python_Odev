# ASAL SAYI KONTROLÜ

def asalMi(sayi):
    sayac=2
    for i in range(2,sayi):
       
       sayac+=1
       if sayi%i==0:
           print("sayi asal degildir")
           
           break
       else:
           if sayac==sayi:
               print("sayi asaldir")
               
           
asalMi(20)







