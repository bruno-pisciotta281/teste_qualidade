import unittest
from jokenpo import jokenpo

class TestJokenpo(unittest.TestCase):

    def test_pedra_vs_pedra_deve_empatar(self):
        resultado = jokenpo("Pedra", "Pedra")
        self.assertEqual(resultado, "Empate")

    def test_pedra_vs_tesoura_deve_vencer_pedra(self):
        resultado = jokenpo("Pedra", "Tesoura")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_tesoura_vs_papel_deve_vencer_tesoura(self):
        resultado = jokenpo("Tesoura", "Papel")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_papel_vs_pedra_deve_vencer_papel(self):
        resultado = jokenpo("Papel", "Pedra")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_tesoura_vs_pedra_deve_vencer_pedra(self):
        resultado = jokenpo("Tesoura", "Pedra")
        self.assertEqual(resultado, "Jogador 2 vence")

    def test_papel_vs_tesoura_deve_vencer_tesoura(self):
        resultado = jokenpo("Papel", "Tesoura")
        self.assertEqual(resultado, "Jogador 2 vence")

    def test_papel_vs_papel_deve_empatar(self):
        resultado = jokenpo("Papel", "Papel")
        self.assertEqual(resultado, "Empate")

    def test_pedra_vs_pedra_deve_empatar(self):
        resultado = jokenpo("Pedra", "Pedra")
        self.assertEqual(resultado, "Empate")

    def test_pedra_vs_tesoura_deve_vencer_pedra(self):
        resultado = jokenpo("Pedra", "Tesoura")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_tesoura_vs_papel_deve_vencer_tesoura(self):
        resultado = jokenpo("Tesoura", "Papel")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_papel_vs_pedra_deve_vencer_papel(self):
        resultado = jokenpo("Papel", "Pedra")
        self.assertEqual(resultado, "Jogador 1 vence")

    def test_pedra_vs_papel_deve_vencer_papel(self):
        resultado = jokenpo("Pedra", "Papel")
        self.assertEqual(resultado, "Jogador 2 vence")

    def test_tesoura_vs_pedra_deve_vencer_pedra(self):
        resultado = jokenpo("Tesoura", "Pedra")
        self.assertEqual(resultado, "Jogador 2 vence")

    def test_papel_vs_tesoura_deve_vencer_tesoura(self):
        resultado = jokenpo("Papel", "Tesoura")
        self.assertEqual(resultado, "Jogador 2 vence")

    # Adicione mais testes aqui

if __name__ == '__main__':
    unittest.main()