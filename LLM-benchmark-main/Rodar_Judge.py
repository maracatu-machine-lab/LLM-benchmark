from openai import OpenAI
import pandas as pd
from LlmJudge import LLMJudge
from transformers import pipeline
from factory import carregar_modelo

#função para chamar o modelo que irá avaliar as respostas
def rodar_judge():
   
   llm = carregar_modelo("medgemma")  

   judge = LLMJudge(llm)

   data = pd.read_csv("dados_medgemma.csv", sep = ";", encoding="utf-8")

   for i, row in data.iterrows():
      resultado = judge.judge(
         correct_answer=row["r_correta"],
         intuitive_answer=row["r_intuitiva"],
         model_answer=row["r_recebida"]
      )

      print(resultado)

      data.loc[i, "r_ajustada"] = resultado.get("final_answer", "-")
      data.loc[i, "idioma"] = resultado.get("language", "indefinido")

   data.to_csv("dados_medgemma_ajustados.csv", sep=";", index=False)
