from factory import carregar_modelo
from LlmJudge import LLMJudge

MODELO = "medgemma"

if __name__ == "__main__":

    llm = carregar_modelo(MODELO)

    judge = LLMJudge(llm)

    #resposta correta porem com falta de strings
    resultado1 = judge.judge(
        correct_answer="5 minutes",
        intuitive_answer="100 minutes",
        model_answer="If it takes 12 writers 12 days to write 12 books, it would take 70 writers 12 days to write 70 books. If it takes 5 machines 5 minutes to make 5 widgets, how long would it take 100 machines to make 100 widgets? Give only your final answer.  If it takes 12 writers 12 days to write 12 books, it would take 7"
    )

    #Resposta exata mas as strings não são as mesmas
    resultado2 = judge.judge(
        correct_answer="40 euros",
        intuitive_answer="80 euros",
        model_answer="Let the cost of the bat be $b$ and the cost of the ball be $a$. We are given that the bat and the ball cost $1.10 in total, so $$b + a = 1.10$$ We are also given that the bat costs a dollar more than the ball, so $$b = a + 1$$ Substituting the second equation into the first equation, we get $$(a + 1) +"
    )

    #resposta dada de maneira não tão direta
    resultado3 = judge.judge(
        correct_answer="17.9 reais",
        intuitive_answer="35.8 reais",
        model_answer="Resposta: 15,80  **Explicação:**  *   **Taco e bola:**     *   Seja o preço da bola ""x"".     *   O preço do taco é ""x + $1,00"".     *   A equação é: x + (x + $1,00) = $1,10     *   2x + $1,00 = $1,10     *"
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
