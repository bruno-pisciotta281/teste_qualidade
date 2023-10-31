import unittest
from distribuicao_mictorios import calcular_mijoes_nao_constrangedores

class TestDistribuicaoMictorios(unittest.TestCase):

    def test_mijoes_nao_constrangedores_1(self):
        ocupacao_inicial = "X...X"
        resultado = calcular_mijoes_nao_constrangedores(ocupacao_inicial)
        self.assertEqual(resultado, 0)

    def test_mijoes_nao_constrangedores_2(self):
        ocupacao_inicial = "X..."
        resultado = calcular_mijoes_nao_constrangedores(ocupacao_inicial)
        self.assertEqual(resultado, 1)

    def test_mijoes_nao_constrangedores_3(self):
        ocupacao_inicial = "...X"
        resultado = calcular_mijoes_nao_constrangedores(ocupacao_inicial)
        self.assertEqual(resultado, 1)

    # Adicione mais testes conforme necessário

if __name__ == '__main__':
    unittest.main()
