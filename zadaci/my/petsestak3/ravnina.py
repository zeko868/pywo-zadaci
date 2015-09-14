
import math #from math import sqrt  - time se uključuje samo ono što nam treba (čak je i bolja od ove obične)

class Tocka: #class naziv_klase(naslijedjena_klasa1,naslijedjena_klasa2,...)
    """
        Opis ove klase.
        2-dim tocke u ravnini.
    """
    def __init__(self,x,y): #ovo je konstruktor klase - u zagradama se mogu navesti argumenti koji se proslijeđuju
                    #objektu pri njegovom alociranju
        self.x=x
        self.y=y
    def norm(self):
        return math.sqrt(self.x**2+self.y**2)
    def __repr__(self):
        return "Tocka({0}, {1})".format(self.x,self.y)
    
class Vektor(Tocka):   #klasa vektor naslijeđuje atribute i metode od klase Tocka
    def __add__(self,b):
        """
        self je vektor, b je vektor
        """
        return Vektor(self.x+b.x , self.y+b.y)
    def __sub__(self,b):
        return Vektor(self.x-b.x , self.y-b.y)
    def __mul__(self,b):
        return Vektor(self.x*b , self.y*b)
    def __rmul__(self,b): #metoda za realizaciju množenja vektora skalarom kad se skalar nalazi ispred vektora
        return Vektor(self.x*b , self.y*b)#time je moguće izračunati 2*a, a ne samo a*2 kao što je sa __mul__ moguće
    def __repr__(self):
        return "Vektor({0}, {1})".format(self.x,self.y)