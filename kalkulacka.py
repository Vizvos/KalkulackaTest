
#Vytvoření třídy kalkulačky

class Kalkulacka:

    def scitani(self, a, b):
        return a + b
    
    def odcitani(self, a, b):
        return a - b
    
    def nasobeni(self, a, b):
        return a * b
    
    def deleni(self, a, b):
        if b == 0:
            raise ValueError("Nelze dělit nulou")
        return a / b
    