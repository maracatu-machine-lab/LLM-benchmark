import pandas as pd

def percentual_acertos(acertos, total):

    if(total != 0):
        por_cento = (acertos/total)*100
        return por_cento
    else:
        return None
    
def idioma_pergunta(titulo):
    titulo = titulo.upper().split("_")

    if "ING" in titulo:
        return "en"
    elif "POR" in titulo:
        return "pt"
    elif "ESP" in titulo:
        return "es"



def analise_resultados(df):
    
    resultados = {"en": {"correta": 0, "intuitiva": 0, "erros": 0, "total": 0, "percentual_acertos": 0.0},
                  "pt": {"correta": 0, "intuitiva": 0, "erros": 0, "total": 0, "percentual_acertos": 0.0},
                  "es": {"correta": 0, "intuitiva": 0, "erros": 0, "total": 0, "percentual_acertos": 0.0}}
    falhas_judge = 0

    for i, linha in df.iterrows():
        idioma_esperado = idioma_pergunta(linha["pergunta"])
        idioma = linha["idioma"].strip()

        if idioma not in resultados:
            falhas_judge += 1
            continue

        if linha["avaliacao"] == "correct":
            resultados[idioma]["correta"] += 1
        elif linha["r_ajustada"] == "intuitive":
            resultados[idioma]["intuitiva"] += 1
        else:
            resultados[idioma]["erros"] += 1

        resultados[idioma]["total"] += 1



    resultados["en"]["percentual_acertos"] = percentual_acertos(resultados["en"]["correta"], resultados["en"]["total"])
    resultados["pt"]["percentual_acertos"] = percentual_acertos(resultados["pt"]["correta"], resultados["pt"]["total"])
    dados_resultados = pd.DataFrame(resultados).T
    return dados_resultados, falhas_judge

dados_1 = pd.read_csv("dados_medgemma_ajustados.csv", sep=";", encoding="utf-8", skiprows=[1, 2])
dados_2 = pd.read_csv("dados_phi-4-mini_ajustados.csv", sep=";", encoding="utf-8", skiprows=[1, 2])

print("\n")
print(analise_resultados(dados_1))
print("\n")
print(analise_resultados(dados_2))
