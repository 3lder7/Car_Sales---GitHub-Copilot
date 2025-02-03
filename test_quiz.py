import unittest
from unittest.mock import patch
from io import StringIO
import quiz

class TestQuiz(unittest.TestCase):

    def setUp(self):
        self.questoes = quiz.questoes

    @patch('builtins.input', side_effect=['1'])
    def test_show_question_correct_answer(self, mock_input):
        questao = self.questoes[0]
        self.assertTrue(quiz.show_question(questao))

    @patch('builtins.input', side_effect=['2'])
    def test_show_question_incorrect_answer(self, mock_input):
        questao = self.questoes[0]
        self.assertFalse(quiz.show_question(questao))

    @patch('builtins.input', side_effect=['5'])
    def test_show_question_invalid_option(self, mock_input):
        questao = self.questoes[0]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(quiz.show_question(questao))
            self.assertIn("Opção inválida. Tente novamente.", fake_out.getvalue())

    @patch('builtins.input', side_effect=['a'])
    def test_show_question_invalid_input(self, mock_input):
        questao = self.questoes[0]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.assertFalse(quiz.show_question(questao))
            self.assertIn("Entrada inválida. Digite um número entre 1 e 4.", fake_out.getvalue())

    def test_verificar_resposta_correct(self):
        questao = self.questoes[0]
        resposta_usuario = "Paris"
        self.assertTrue(quiz.verificar_resposta(questao, resposta_usuario))

    def test_verificar_resposta_incorrect(self):
        questao = self.questoes[0]
        resposta_usuario = "Londres"
        self.assertFalse(quiz.verificar_resposta(questao, resposta_usuario))

if __name__ == '__main__':
    unittest.main()