from pergunta import Pergunta

originais_ingles = [
    Pergunta("A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. How much does the ball cost?", "5 cents", "10 cents", "2005"),
]

originais_portugues = [
    Pergunta("Um taco e uma bola custam $1,10 no total. O taco costa um dólar a mais que a bola. Quanto custa a bola?", "5 centavos", "10 centavos", "2005"),
]
originais_ex_ingles = [
    Pergunta("A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. The painting costs 17.9 dollars. A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. How much does the ball cost?", "5 cents", "10 cents", "2005/2025"),
]

originais_ex_portugues = [
    Pergunta("Um espelho e um quadro custam R$50,80 no total, se o espelho custa quinze reais a mais que o quadro, o quadro custa R$17,9. Um taco e uma bola custam $1,10 no total. O taco costa um dólar a mais que a bola. Quanto custa a bola?", "5 centavos", "10 centavos", "2005/2025"),
]

novas_ingles = [
    Pergunta("A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. How much does the painting cost?", "17.9 dollars", "35.8 dollars", "2025"),
 ]

novas_portugues = [
    Pergunta("Um espelho e um quadro custam R$50,80 no total. O espelho custa quinze reais a mais que o quadro. Quanto custa o quadro?", "17.9 reais", "35.8 reais", "2025"),
]

novas_ex_ingles = [
    Pergunta("A bat and a ball cost $1.10 in total. The bat costs a dollar more than the ball. The ball costs 5 cents. A mirror and a painting cost 50.80 dollars in total. The mirror costs fifteen dollars more than the painting. How much does the painting cost?", "17.9 dollars", "35.8 dollars", "2025/2005"),
 ]

novas_ex_portugues = [
    Pergunta("Um taco e uma bola custam $1,10 no total. Se o taco costa um dólar a mais que a bola, a bola custa 5 centavos. Um espelho e um quadro custam R$50,80 no total. O espelho custa quinze reais a mais que o quadro. Quanto custa o quadro?", "17.9 reais", "35.8 reais", "2025/2005"),
  ]

configuracoes_perguntas = [
    {
        "lista": originais_ingles,
        "titulo": "Pergunta original - Inglês",
        "complemento": " Give only your final answer.",
        "id": "ORIG_ING_"
    },
    {
        "lista": originais_portugues,
        "titulo": "Pergunta original - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "ORIG_POR_"
    },
    {
        "lista": originais_ex_ingles,
        "titulo": "Pergunta original com exemplo - Inglês",
        "complemento": " Give only your final answer.",
        "id": "ORIG_EX_ING_"
    },
    {
        "lista": originais_ex_portugues,
        "titulo": "Pergunta original com exemplo - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "ORIG_EX_POR_"
    },
    {
        "lista": novas_ingles,
        "titulo": "Pergunta nova - Inglês",
        "complemento": " Give only your final answer.",
        "id": "NOVA_ING_"
    },
    {
        "lista": novas_portugues,
        "titulo": "Pergunta nova - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "NOVA_POR_"
    },
    {
        "lista": novas_ex_ingles,
        "titulo": "Pergunta nova com exemplo - Inglês",
        "complemento": " Give only your final answer.",
        "id": "NOVA_EX_ING_"
    },
    {
        "lista": novas_ex_portugues,
        "titulo": "Pergunta nova com exemplo - Português",
        "complemento": " Dê apenas sua resposta final.",
        "id": "NOVA_EX_POR_"
    },
]