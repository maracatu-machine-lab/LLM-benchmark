import numpy as np
import pandas as pd
from colorama import Fore
import concurrent.futures

from factory import carregar_modelo
from perguntas import configuracoes_perguntas
from graficos import gerar_graficos
from factory import MODELOS_DISPONIVEIS
from propriedades_configuracao import settings

#MODELOS = list(MODELOS_DISPONIVEIS.keys())
print("modelos disponíveis: ", MODELOS_DISPONIVEIS.keys())
MODELOS = ['medgemma']
NUMERO_ITERACOES = settings.numero_iteracoes

pergunta_arr = ['pergunta']
origem_arr = ['origem']
modelo_arr = ['modelo']
resposta_correta_arr = ['r_correta']
resposta_intuitiva_arr = ['r_intuitiva']
resposta_recebida_arr = ['r_recebida']
resposta_ajustada_arr = ['r_ajustada']
idioma_resposta_arr = ['idioma']
avaliacao_arr = ['avaliacao']


def obter_resposta_do_modelo(llm, prompt, timeout_in_seconds=settings.timeout_in_seconds):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(llm.generate, prompt)
        try:
            return future.result(timeout=timeout_in_seconds)
        except concurrent.futures.TimeoutError:fazer_perguntas(
            config["lista"],
            config["titulo"],
            config["complemento"],
            config["id"],
            llm,
            nome_modelo
        )
        return "TEMPO_LIMITE_EXCEDIDO"

def fazer_perguntas(array_perguntas, texto_titulo_pergunta, complemento_pergunta, texto_id_pergunta, llm, nome_modelo):
  for indice_pergunta, pergunta in enumerate(array_perguntas):
    print("-------------------------------------")
    print("-------------------------------------")
    print("-------------------------------------")
    print(texto_titulo_pergunta)
    print(pergunta.pergunta)

    prompt = pergunta.pergunta + complemento_pergunta

    for i in range(NUMERO_ITERACOES):
        response = obter_resposta_do_modelo(llm, prompt)
        response = str(response)

        print("Modelo: " + nome_modelo + "       Resposta número: " + str(i+1))
        print(Fore.GREEN + "Resposta correta: " + pergunta.resposta_correta)
        print(Fore.RED + "Resposta intuitiva: " + pergunta.resposta_intuitiva)
        print(Fore.BLACK + response)

        pergunta_arr.append(texto_id_pergunta + str(indice_pergunta+1))
        origem_arr.append(pergunta.origem)
        modelo_arr.append(nome_modelo)
        resposta_correta_arr.append(pergunta.resposta_correta)
        resposta_intuitiva_arr.append(pergunta.resposta_intuitiva)
        resposta_recebida_arr.append((" ".join(response.splitlines())).replace(";", ","))
        resposta_ajustada_arr.append("")
        idioma_resposta_arr.append("")
        avaliacao_arr.append("")


# -------------
# FAZER PERGUNTAS
for nome_modelo in MODELOS:
    llm = carregar_modelo(nome_modelo)
    for config in configuracoes_perguntas:
        fazer_perguntas(
            config["lista"],
            config["titulo"],
            config["complemento"],
            config["id"],
            llm,
            nome_modelo
        )

# -------------
# CRIAÇÃO DO ARQUIVO CSV

np.savetxt('dados_medgemma.csv', np.c_[pergunta_arr, origem_arr, modelo_arr, resposta_correta_arr, resposta_intuitiva_arr, resposta_recebida_arr, resposta_ajustada_arr, idioma_resposta_arr, avaliacao_arr], delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s'])

# -------------
# AVALIAÇÃO A SER FEITA APÓS O TRATAMENTO DAS RESPOSTAS
# !!! OS ARQUIVOS TRATADOS DEVEM TER '_ajustados' no fim do nome para o código a seguir funcionar sem modificações


data = pd.read_csv('dados_medgemma_ajustados.csv', sep=";", keep_default_na=False)
data['avaliacao'] = np.where(data['r_ajustada'] == data['r_correta'], 'correta', np.where(data['r_ajustada'] == data['r_intuitiva'], 'intuitiva', np.where(data['r_ajustada'] == '-', 'nao_respondida', 'outro')))
data.to_csv('dados_medgemma_avaliados.csv',index=False, sep=";")

# -------------
# JUNÇÃO DOS ARQUIVOS AVALIADOS DE TODAS AS LLMS

resultado = []

df = pd.read_csv('dados_medgemma_avaliados.csv', sep=";", keep_default_na=False)
resultado.append(df)

frame = pd.concat(resultado, axis=0, ignore_index=True)
frame.to_csv('dados_tcc_todos_avaliados.csv', index=False, sep=";")


# -------------
# CRIAÇÃO DE GRÁFICOS
gerar_graficos(MODELOS)