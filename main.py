import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore
from openai import OpenAI
from perguntas import configuracoes_perguntas

models = ["qwen3.5-4b"]
all_models = models

TEMPERATURA = 0.7
NUMERO_ITERACOES = 10

pergunta_arr = ['pergunta']
origem_arr = ['origem']
modelo_arr = ['modelo']
resposta_correta_arr = ['r_correta']
resposta_intuitiva_arr = ['r_intuitiva']
resposta_recebida_arr = ['r_recebida']
resposta_ajustada_arr = ['r_ajustada']
idioma_resposta_arr = ['idioma']
avaliacao_arr = ['avaliacao']

def fazer_perguntas(array_perguntas, texto_titulo_pergunta, complemento_pergunta, texto_id_pergunta):
  
  client = OpenAI(
      base_url="http://localhost:1234/v1",
      api_key="lm-studio"  # qualquer string funciona
  )

  used_models = models
 
  for indice_pergunta, pergunta in enumerate(array_perguntas):
    print("-------------------------------------")
    print("-------------------------------------")
    print("-------------------------------------")
    print(texto_titulo_pergunta)
    print(pergunta.pergunta)

    messages = [
        {"role": "user",
        "content": (pergunta.pergunta + complemento_pergunta)}
    ]

    for model in used_models:
      for i in range(NUMERO_ITERACOES):
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=TEMPERATURA,
            #max_tokens=50 # Pode ser removido
        )

        print("-------------------------------------")
        print("Modelo: " + model + "       Resposta número: " + str(i+1))
        print(Fore.GREEN + "Resposta correta: " + pergunta.resposta_correta)
        print(Fore.RED + "Resposta intuitiva: " + pergunta.resposta_intuitiva)
        print(Fore.BLACK + response.choices[0].message.content)

        pergunta_arr.append(texto_id_pergunta + str(indice_pergunta+1))
        origem_arr.append(pergunta.origem)
        modelo_arr.append(model)
        resposta_correta_arr.append(pergunta.resposta_correta)
        resposta_intuitiva_arr.append(pergunta.resposta_intuitiva)
        resposta_recebida_arr.append((" ".join(response.choices[0].message.content.splitlines())).replace(";", ","))
        resposta_ajustada_arr.append("")
        idioma_resposta_arr.append("")
        avaliacao_arr.append("")


# -------------
# FAZER PERGUNTAS
for config in configuracoes_perguntas:
    fazer_perguntas(
        config["lista"],
        config["titulo"],
        config["complemento"],
        config["id"]
    )


# -------------
# CRIAÇÃO DO ARQUIVO CSV

np.savetxt('dados_qwen.csv', np.c_[pergunta_arr, origem_arr, modelo_arr, resposta_correta_arr, resposta_intuitiva_arr, resposta_recebida_arr, resposta_ajustada_arr, idioma_resposta_arr, avaliacao_arr], delimiter=';', fmt=['%s','%s','%s','%s','%s','%s','%s','%s','%s'])

# -------------
# AVALIAÇÃO A SER FEITA APÓS O TRATAMENTO DAS RESPOSTAS
# !!! OS ARQUIVOS TRATADOS DEVEM TER '_ajustados' no fim do nome para o código a seguir funcionar sem modificações


data = pd.read_csv('dados_qwen_ajustados.csv', sep=";", keep_default_na=False)
data['avaliacao'] = np.where(data['r_ajustada'] == data['r_correta'], 'correta', np.where(data['r_ajustada'] == data['r_intuitiva'], 'intuitiva', np.where(data['r_ajustada'] == '-', 'nao_respondida', 'outro')))
data.to_csv('dados_qwen_avaliados.csv',index=False, sep=";")

# -------------
# JUNÇÃO DOS ARQUIVOS AVALIADOS DE TODAS AS LLMS

resultado = []

df = pd.read_csv('dados_qwen_avaliados.csv', sep=";", keep_default_na=False)
resultado.append(df)

frame = pd.concat(resultado, axis=0, ignore_index=True)
frame.to_csv('dados_tcc_todos_avaliados.csv', index=False, sep=";")


# -------------
# CRIAÇÃO DE GRÁFICOS

# Idioma de resposta por modelo

data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)

grafico = pd.crosstab(data['modelo'], data['idioma']).plot.bar(stacked=True, color=['red', 'gold'])
grafico.set_ylabel('nº de respostas')
grafico.legend(["inglês", "português"], title='idioma da resposta', bbox_to_anchor=(1.0, 1), loc='upper left')

for rec in grafico.patches:
    height = rec.get_height()
    grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

plt.savefig('grafico_idioma_resposta_por_modelo.png', bbox_inches='tight')
plt.show()

# Idioma de resposta por tipo de pergunta por modelo

data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)

for model in all_models:
  data_modelo = data[data['modelo'] == model]

  grafico = pd.crosstab(data_modelo['pergunta'].str.rpartition("_")[0], data_modelo['idioma']).plot.bar(stacked=True, color=['red', 'gold'])
  grafico.set_title(model)
  grafico.set_ylabel('nº de respostas')
  grafico.set_xlabel('tipo de pergunta')
  grafico.legend(["inglês", "português"], title='idioma da resposta', bbox_to_anchor=(1.0, 1), loc='upper left')

  for rec in grafico.patches:
      height = rec.get_height()
      grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

  plt.savefig('grafico_idioma_resposta_por_tipo_pergunta_' + model +'.png', bbox_inches='tight')
  plt.show()

# Avaliação por modelo

data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)

grafico = pd.crosstab(data['modelo'], data['avaliacao']).plot.bar(stacked=True)
grafico.set_ylabel('nº de respostas')
grafico.legend(title='avaliação recebida', bbox_to_anchor=(1.0, 1), loc='upper left')

for rec in grafico.patches:
    height = rec.get_height()
    grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

plt.savefig('grafico_avaliacao_por_modelo.png', bbox_inches='tight')
plt.show()

# Avaliação por tipo de pergunta por modelo

data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)

for model in all_models:
  data_modelo = data[data['modelo'] == model]

  grafico = pd.crosstab(data_modelo['pergunta'].str.rpartition("_")[0], data_modelo['avaliacao']).plot.bar(stacked=True)
  grafico.set_title(model)
  grafico.set_ylabel('nº de respostas')
  grafico.set_xlabel('tipo de pergunta')

  for rec in grafico.patches:
      height = rec.get_height()
      grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

  plt.savefig('grafico_resposta_por_tipo_pergunta_' + model +'.png', bbox_inches='tight')
  plt.show()

# Avaliação por tipo de pergunta

def acertos_tipo_pergunta(tipo_pergunta, id_pergunta):
  data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)
  data_perguntas = data[data['pergunta'].str.startswith(id_pergunta + '_')]

  grafico = pd.crosstab(data_perguntas['modelo'], data_perguntas['avaliacao']).plot.bar(stacked=True)
  grafico.set_title(tipo_pergunta)
  grafico.set_ylabel('nº de respostas')
  grafico.legend(title='avaliação recebida', bbox_to_anchor=(1.0, 1), loc='upper left')

  for rec in grafico.patches:
      height = rec.get_height()
      grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

  plt.savefig('grafico_avaliacao_tipo_pergunta_' + id_pergunta.lower() + '.png', bbox_inches='tight')
  plt.show()

acertos_tipo_pergunta('original inglês', 'ORIG_ING')
acertos_tipo_pergunta('original português', 'ORIG_POR')
acertos_tipo_pergunta('original inglês com exemplo', 'ORIG_EX_ING')
acertos_tipo_pergunta('original português com exemplo', 'ORIG_EX_POR')
acertos_tipo_pergunta('nova inglês', 'NOVA_ING')
acertos_tipo_pergunta('nova português', 'NOVA_POR')
acertos_tipo_pergunta('nova inglês com exemplo', 'NOVA_EX_ING')
acertos_tipo_pergunta('nova português com exemplo', 'NOVA_EX_POR')

# Avaliação por pergunta por modelo

def acertos_pergunta_modelo(tipo_pergunta, id_pergunta):
  data = pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)

  for model in all_models:
    data_modelo = data[data['modelo'] == model]
    data_modelo = data_modelo[data_modelo['pergunta'].str.startswith(id_pergunta + '_')]

    ids_perguntas = data_modelo['pergunta'].unique()
    data_modelo['pergunta'] = pd.Categorical(data_modelo['pergunta'], ids_perguntas)

    grafico = pd.crosstab(data_modelo['pergunta'], data_modelo['avaliacao']).sort_index().plot.bar(stacked=True)
    grafico.set_title(model)
    grafico.set_ylabel('número de respostas - ' + tipo_pergunta)
    grafico.legend(title='avaliação recebida', bbox_to_anchor=(1.0, 1), loc='upper left')

    for rec in grafico.patches:
        height = rec.get_height()
        grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

    plt.savefig('grafico_avaliacao_por_pergunta_' + id_pergunta.lower() + '_' + model +'.png', bbox_inches='tight')
    plt.show()

acertos_pergunta_modelo('originais inglês', 'ORIG_ING')
acertos_pergunta_modelo('originais português', 'ORIG_POR')
acertos_pergunta_modelo('originais inglês com exemplo', 'ORIG_EX_ING')
acertos_pergunta_modelo('originais português com exemplo', 'ORIG_EX_POR')
acertos_pergunta_modelo('novas inglês', 'NOVA_ING')
acertos_pergunta_modelo('novas português', 'NOVA_POR')
acertos_pergunta_modelo('novas inglês com exemplo', 'NOVA_EX_ING')
acertos_pergunta_modelo('novas português com exemplo', 'NOVA_EX_POR')
