import unittest
from src.modell.Modell import HipotecaInversa

class TestHipotecaInversa(unittest.TestCase):

    def setUp(self):
        self.hipoteca = HipotecaInversa(valor_vivienda=300000, edad=65, interes_anual=4.5, renta_mensual=1000)

    def test_hipoteca_inversa_temporal(self):
        resultado = self.hipoteca.hipoteca_inversa_temporal(10)
        self.assertAlmostEqual(resultado, 154877.15, places=2)

    def test_hipoteca_inversa_vitalicia(self):
        resultado = self.hipoteca.hipoteca_inversa_vitalicia(20)
        self.assertAlmostEqual(resultado, 300000, places=2)

    def test_hipoteca_inversa_unica(self):
        deuda, meses = self.hipoteca.hipoteca_inversa_unica()
        self.assertAlmostEqual(deuda, 300000, places=2)
        self.assertEqual(meses, 211)

if __name__ == '__main__':
    unittest.main()
