from openai import OpenAI
import pandas as pd
from LlmJudge import LLMJudge

#função para chamar o modelo que irá avaliar as respostas
def rodar_judge():
   
   client = OpenAI(
      base_url = "http://localhost:12434/v1",
      api_key = "local"
   )

   judge = LLMJudge(client, "llama3.2:1B-F16")

   data = pd.read_csv("dados_qwen.csv", sep = ";", encoding="utf-8")

   for i, row in data.iterrows():
      resultado = judge.judge(
        question = row["pergunta"],
        correct_answer = row["r_correta"],
        intuitive_answer = row["r_intuitiva"],
        model_answer = row["r_recebida"]
      )

      print(resultado)

      data.loc[i, "r_ajustada"] = resultado.get("final_answer", "-")
      data.loc[i, "idioma"] = resultado.get("language", "indefinido")
      data.loc[i, "avaliacao"] = resultado.get("classification", "outro")
      

   data.to_csv("dados_qwen_ajustados.csv", sep=";", index=False)