import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    a = 5
    b = 9
    c = 10
    
    def test_operacao_soma(self):
        """
        Testa se a função de soma consegue somar corretamente
        """
        resultado = Calculadora.soma(self.a, self.b)
        self.assertEqual(resultado, 14)

    def test_operacao_subtracao(self):
        """
        Testa se a função de subtração consegue subtrair corretamente
        """
        resultado = Calculadora.subtracao(self.b, self.a)
        self.assertEqual(resultado, 4)

    def test_operacao_divisao(self):
        """
        Testa se a função de divisão consegue dividir corretamente
        """
        resultado = Calculadora.divisao(self.c, self.a)
        self.assertEqual(resultado, 2)

    def test_operacao_multiplicacao(self):
        """
        Testa se a função de multiplicação consegue multiplicar corretamente
        """
        resultado = Calculadora.multiplicacao(self.a, self.b)
        self.assertEqual(resultado, 45)


if __name__ == '__main__':
    unittest.main()
