import math

class Ulamek:
    
    # Wersja2 __slots__ = ('licznik', 'mianownik')
     
    def __init__(self, licznik, mianownik):
        assert mianownik != 0
        self.l = licznik // math.gcd(licznik, mianownik)
        self.m = mianownik // math.gcd(licznik, mianownik)
        
    def __add__(self, inny):
        l2 = inny.l
        m2 = inny.m
        
        wynikl = self.l * m2 + self.m * l2
        wynikm = self.m * m2

        return Ulamek(wynikl // math.gcd(wynikl, wynikm), wynikm // math.gcd(wynikl, wynikm))    
        
    def __sub__(self, inny):
        l2 = inny.l
        m2 = inny.m
        
        wynikl = self.l * m2 - self.m * l2
        wynikm = self.m * m2

        return Ulamek(wynikl // math.gcd(wynikl, wynikm), wynikm // math.gcd(wynikl, wynikm))
    
    def __mul__(self, inny):
        l2 = inny.l
        m2 = inny.m
        wynikl = self.l * l2
        wynikm = self.m * m2 
        return Ulamek(wynikl // math.gcd(wynikl, wynikm), wynikm // math.gcd(wynikl, wynikm))
    
    def __truediv__(self, inny):
        l2 = inny.l
        m2 = inny.m
        assert(l2 != 0)
        wynikl = self.l * m2
        wynikm = self.m * l2
        return Ulamek(wynikl // math.gcd(wynikl, wynikm), wynikm // math.gcd(wynikl, wynikm))
        
        
    def __str__(self): ##wypisz liczbe
        if self.ujemny() == True:
            if self.modul(self.m) != 1:
                return f"- {self.modul(int(self.l))} / {self.modul(int(self.m))}"
            else:
                return f"- {self.modul(int(self.l))}"   
        else:
            if self.m != 1:
                return f"{int(self.l)} / {int(self.m)}"
            else:
                return f"{int(self.l)}"
    
    def ujemny(self):
        if self.l < 0 and self.m > 0:
            return True
        if self.l > 0 and self.m < 0:
            return True
        return False
    
    def modul(self, a):
        if a > 0:
            return a
        else:
            return -a
        
