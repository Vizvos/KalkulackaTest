import unittest # import unittest knihovny pro testování 
from kalkulacka import Kalkulacka # import třídy kalkulačka 


# Definování unittestu pro kalkulačku
class TestKalkulacka(unittest.TestCase):
    def setUp(self):
        self.kalkulacka = Kalkulacka() 

    def test_scitani(self):
        self.assertEqual(self.kalkulacka.scitani(2, 3), 5)

    def test_odcitani(self):
        self.assertEqual(self.kalkulacka.odcitani(5, 3), 2)

    def test_nasobeni(self):
        self.assertEqual(self.kalkulacka.nasobeni(4, 3), 12)

    def test_deleni(self):
        self.assertEqual(self.kalkulacka.deleni(10, 2), 5)

    def test_deleni_nulou(self):
        with self.assertRaises(ValueError): #očekáváme že se vrátí Error
            self.kalkulacka.deleni(5, 0)

if __name__ == '__main__':
    unittest.main()