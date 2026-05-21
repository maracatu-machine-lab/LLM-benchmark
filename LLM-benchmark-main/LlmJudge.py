from converter_json import converter
class LLMJudge:
    def __init__(self, llm):
        self.llm = llm

    def judge(self, correct_answer, intuitive_answer, model_answer):

        prompt = f"""
            You are an evaluator of candidate answers. Your main task is to compare the answer given by the candidate: {model_answer}
            and determine whether it matches the correct answer: {correct_answer}, whether it matches the intuitive answer: {intuitive_answer},
            whether the answer is incorrect, or whether the candidate did not provide an answer. You must also determine the language of the response.

            Your tasks include:
            1 - Analyze the candidate's response and its context, then extract the final answer.
            2 - Classify the response as:
            - correct
            - intuitive
            - other (if the answer is incorrect)
            - unanswered (if there is no valid answer)

            Language rules:
            - "pt" for Portuguese
            - "en" for English
            - "es" for Spanish
            - "other" for another language
            - "undefined" if the language cannot be determined

            Return ONLY valid JSON in the following format:
            {{
                "final_answer": "...",
                "classification": "correct|intuitive|other|unanswered",
                "language": "pt|en|es|other|undefined"
            }}

            Correct answer: {correct_answer}
            Intuitive answer: {intuitive_answer}

            Model response:
            {model_answer}
            """

        texto = self.llm.generate(prompt, max_tokens=1000)

        print("\n_______REPOSTA MODELO BRUTA___________\n")
        print(texto)
        print("\n---------------------------------------\n")

        return converter(texto)

