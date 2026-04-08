import unittest
from LlmJudge import LLMJudge

class FakeMessage:
    def __init__(self, content):
        self.content = content

class FakeChoice:
    def __init__(self, content):
        self.message = FakeMessage(content)

class FakeResponse:
    def __init__(self, content):
        self.choices = [FakeChoice(content)]

class FakeCompletions:
    def __init__(self, content):
        self.content = content

    def create(self, model, messages, temperature):
        return FakeResponse(self.content)

class FakeChat:
    def __init__(self, content):
        self.completions = FakeCompletions(content)

class FakeClient:
    def __init__(self, content):
        self.chat = FakeChat(content)


class TestLLMJudge(unittest.TestCase):

    def test_json_valido(self):
        conteudo = '''
        {
            "final_answer": "5 cents",
            "language": "en",
            "classification": "correta"
        }
        '''

        client_falso = FakeClient(conteudo)
        judge = LLMJudge(client_falso, "modelo-fake")

        resultado = judge.judge(
            question="A bat and a ball cost $1.10 in total...",
            correct_answer="5 cents",
            intuitive_answer="10 cents",
            model_answer="The answer is 5 cents."
        )

        self.assertEqual(resultado["final_answer"], "5 cents")
        self.assertEqual(resultado["language"], "en")
        self.assertEqual(resultado["classification"], "correta")

    def test_json_invalido(self):
        conteudo = "resposta fora do formato"

        client_falso = FakeClient(conteudo)
        judge = LLMJudge(client_falso, "modelo-fake")

        resultado = judge.judge(
            question="2+2?",
            correct_answer="4",
            intuitive_answer="4",
            model_answer="acho que é 4"
        )

        self.assertEqual(resultado["final_answer"], "-")
        self.assertEqual(resultado["language"], "indefinido")
        self.assertEqual(resultado["classification"], "outro")


if __name__ == "__main__":
    unittest.main()