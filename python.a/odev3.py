#sınıflar

class Human:
    name = "Ceyda"
    
    def __init__(self,name):
        print("Bir human instance üretildi")#constructor alanı gibi
        self.name=name



    def talk(self):  
        name="Ankara"
        print(f" {name} Human is talking")
      

 
    def walk(self, sentence):

        print(f"Human is walking {sentence}")



human1 = Human("Ceyda")
human1.talk()  
human1.walk("ben") 

  
def topla(a,b):
    return a+b

def bol(a,b):
    return a/b

   
