import pandas as pd
from LlmJudge import LLMJudge
from transformers import pipeline
from factory import carregar_modelo


#função para chamar o modelo que irá avaliar as respostas
def rodar_judge():

   modelo_juiz = ["phi-4-mini", "medgemma"]
   for x in modelo_juiz:
      llm = carregar_modelo(x)  
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
         data.loc[i, "avaliacao"] = resultado.get("classification", "sem_resultado")
         data.loc[i, "modelo_juiz"] = x

      data.to_csv(f"dados_{x}_ajustados.csv", sep=";", index=False)
