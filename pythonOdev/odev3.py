
for i in range(1,100):
 print(i)

print("*****************")

for i in range(0,100,2):
 print(i)

print("*****************")

sayi=int(input("Sayi giriniz: "))

a=1
for i in range(1,sayi+1):
    a=a*i
print(a)


 for i in range(2, 100):  
    
    for j in range(2, int(i ** 0.5) + 1): 
        if i % j == 0:
            asal_mi = False  
            break  
    
    if asal_mi:
        print(i, "asal sayıdır.")
     


