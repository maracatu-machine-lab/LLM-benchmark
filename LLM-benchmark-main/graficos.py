import pandas as pd
import matplotlib.pyplot as plt

# Idioma de resposta por modelo
def grafico_idioma_por_modelo(data):
  grafico = pd.crosstab(data['modelo'], data['idioma']).plot.bar(stacked=True, color=['red', 'gold'])
  grafico.set_ylabel('nº de respostas')
  grafico.legend(["inglês", "português"], title='idioma da resposta', bbox_to_anchor=(1.0, 1), loc='upper left')

  for rec in grafico.patches:
      height = rec.get_height()
      grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

  plt.savefig('grafico_idioma_resposta_por_modelo.png', bbox_inches='tight')
  plt.show()


# Idioma de resposta por tipo de pergunta por modelo
def grafico_idioma_por_tipo_pergunta(data, all_models):
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
def grafico_avaliacao_por_modelo(data):
  grafico = pd.crosstab(data['modelo'], data['avaliacao']).plot.bar(stacked=True)
  grafico.set_ylabel('nº de respostas')
  grafico.legend(title='avaliação recebida', bbox_to_anchor=(1.0, 1), loc='upper left')

  for rec in grafico.patches:
      height = rec.get_height()
      grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

  plt.savefig('grafico_avaliacao_por_modelo.png', bbox_inches='tight')
  plt.show()


# Avaliação por tipo de pergunta por modelo
def acertos_tipo_pergunta_por_modelo(data, all_models):
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
def acertos_tipo_pergunta(data, tipo_pergunta, id_pergunta):
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


# Avaliação por pergunta por modelo
def acertos_pergunta_modelo(data, todos_modelos, tipo_pergunta, id_pergunta):
  for modelo in todos_modelos,:
    data_modelo = data[data['modelo'] == modelo]
    data_modelo = data_modelo[data_modelo['pergunta'].str.startswith(id_pergunta + '_')]

    ids_perguntas = data_modelo['pergunta'].unique()
    data_modelo['pergunta'] = pd.Categorical(data_modelo['pergunta'], ids_perguntas)

    grafico = pd.crosstab(data_modelo['pergunta'], data_modelo['avaliacao']).sort_index().plot.bar(stacked=True)
    grafico.set_title(modelo)
    grafico.set_ylabel('número de respostas - ' + tipo_pergunta)
    grafico.legend(title='avaliação recebida', bbox_to_anchor=(1.0, 1), loc='upper left')

    for rec in grafico.patches:
        height = rec.get_height()
        grafico.text(rec.get_x() + rec.get_width() / 2, rec.get_y() + height / 2, "{:.0f}".format(height), ha='center', va='bottom')

    plt.savefig('grafico_avaliacao_por_pergunta_' + id_pergunta.lower() + '_' + modelo +'.png', bbox_inches='tight')
    plt.show()



def carregar_dados():
    return pd.read_csv('dados_tcc_todos_avaliados.csv', sep=";", keep_default_na=False)


def gerar_graficos(todos_modelos):
  data = carregar_dados()

  grafico_idioma_por_modelo(data)
  grafico_idioma_por_tipo_pergunta(data, todos_modelos)
  grafico_avaliacao_por_modelo(data)
  acertos_tipo_pergunta_por_modelo(data, todos_modelos)

  tipos_perguntas = [
     ("original inglês", "ORIG_ING"),
     ("original português", "ORIG_POR"),
     ("original inglês com exemplo", "ORIG_EX_ING"),
     ("original português com exemplo", "ORIG_EX_POR"),
     ("nova inglês", "NOVA_ING"),
     ("nova português", "NOVA_POR"),
     ("nova inglês com exemplo", "NOVA_EX_ING"),
     ("nova português com exemplo", "NOVA_EX_POR"),
    ]

  for nome, id_pergunta in tipos_perguntas:
    acertos_tipo_pergunta(data, nome, id_pergunta)
    acertos_pergunta_modelo(data, todos_modelos, nome, id_pergunta)