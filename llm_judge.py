import json

class LLMJudge:
    def __init__(self, client, judge_model):
        self.client = client
        self.judge_model = judge_model

    def judge(self, question, correct_answer, intuitive_answer, model_answer):

        prompt = f"""
        você é um avaliador de respostas de modelos de linguagem.
        pergunta: {question} 
        resposta correta: {correct_answer}
        resposta intuitiva: {intuitive_answer}
        resposta do modelo: {model_answer}

        suas tarefas:
        1 - extrair APENAS a resposta final dada pelo modelo
        2 - classifique como:
        - correta
        - intuitiva
        - outro
        - nao_respondida

        Regras para idioma:
        - "pt" para Portugês
        - "en" para Inglês
        - "outro" para outro idioma
        - "indefinido" se não der para saber
        
        Responda somente em JSON:
        
        {{
            "final_answer": "...",
            "language": "...",
            "classification": "..."
        }}
        """
        response = self.client.chat.completions.create(
           model = self.judge_model,
           messages = [{"role" : "user", "content": prompt}],
           temperature = 0
        )
        content = response.choices[0].message.content

        try:
            resultado = json.loads(content)
            valid_classifications = ["correta", "intuitiva", "outro", "nao_respondida"]
            valid_languages = ["pt", "en", "outro", "indefinido"]

            if resultado.get("classification") not in valid_classifications:
                resultado["classification"] = "outro"

            if resultado.get("language") not in valid_languages:
                resultado["language"] = "indefinido"

            if not resultado.get("final_answer"):
                resultado["final_answer"] = "-"
        except:
            resultado = {"final_answer": "-",
                         "language": "indefinido",
                         "classification": "outro",
                         }
        return resultado

