from factory import carregar_modelo
from LlmJudge import LLMJudge

MODELO = "medgemma"

if __name__ == "__main__":

    llm = carregar_modelo(MODELO)

    judge = LLMJudge(llm)

    #resposta correta porem com falta de strings
    resultado1 = judge.judge(
        correct_answer="11 cents",
        intuitive_answer="8 cents",
        model_answer="7 cents would be the first answer, but I realized 3 were missing from the calculation, so the correct answer is 10."
    )

    #Resposta exata mas as strings não são as mesmas
    resultado2 = judge.judge(
        correct_answer="10 horas",
        intuitive_answer="7 horas",
        model_answer="fique reciocinando e chegei a coclusão que 7 horas é o tempo certo."
    )

    #resposta dada de maneira não tão direta
    resultado3 = judge.judge(
        correct_answer="37 reais",
        intuitive_answer="40 reais",
        model_answer="ao analisar a questão em si, percebi 40 seria a resposta idela, mas percebi qie deveria tirar 3 da conta e passo a dizer que é 37."
    )

    print("\nresultado do judge:")
    print("\n")
    print("-----------------------------------------------------------------------")
    print(resultado1)
    print("\n")
    print("-----------------------------------------------------------------------")
    print(resultado2)
    print("\n")
    print("-----------------------------------------------------------------------")
    print(resultado3)
