from factory import carregar_modelo
from LlmJudge import LLMJudge
import time

MODELO = "medgemma"
PERGUNTA = "If Anna can paint a room in 3 hours and Bob can paint a room in 6 hours, how many hours would it take for them to paint a room together?"
RESPOSTA_CORRETA = "2 hours"
RESPOSTA_INTUITIVA = "4.5 hours"

if __name__ == "__main__":

    llm = carregar_modelo(MODELO)

    judge = LLMJudge(llm)

    inicio_time = time.time()

    resposta_modelo = llm.generate(PERGUNTA)

    fim_time = time.time()
    tempo = fim_time - inicio_time

    print(f"tempo de resposta: {tempo} segundos")

    print("\nresposta do modelo:")
    print(resposta_modelo)

    resultado = judge.judge(
        correct_answer=RESPOSTA_CORRETA,
        intuitive_answer=RESPOSTA_INTUITIVA,
        model_answer=resposta_modelo
    )

    print("\nresultado do judge:")
    print(resultado)