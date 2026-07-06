from converter_json import converter
class LLMJudge:
    def __init__(self, llm):
        self.llm = llm

    def judge(self, correct_answer, intuitive_answer, model_answer):

        prompt = f"""
            You are a strict, literal evaluator of candidate answers. You do NOT solve the
            problem yourself and you do NOT infer what the answer "should" be. You only
            extract what the candidate actually wrote and compare it to the reference answers.
            
            Note: the candidate_response may contain LaTeX notation (symbols like $, \\cdot,
            _, ^, \\boxed{{}}, etc.). Treat this as normal mathematical text, not as a
            formatting error or sign of an incomplete/broken response.

            <reference_answers>
            Correct answer: {correct_answer}
            Intuitive (common wrong) answer: {intuitive_answer}
            </reference_answers>
            
            <candidate_response>
            {model_answer}
            </candidate_response>
            
            Your tasks:
            1. Read ONLY the candidate_response above. Ignore any other problem, context,
               or reasoning that is not explicitly part of this response.

            2. Extract the final answer the candidate actually gave — copy it verbatim
               (or the closest verbatim numeric/short phrase) from the text. 
               Do NOT invent, complete, or infer an answer that is not explicitly stated.

            3. If the response is truncated, repeats the question, or the reasoning
               never reaches an explicit final answer, the correct classification is
               "unanswered" — even if the reasoning trend suggests where it was heading.

            4. Compare the extracted final_answer to the reference answers:
               - Treat numerically/semantically equivalent forms as a match
                 (e.g. "12" and "12 days" are equivalent if the unit is implied elsewhere
                 in the question; "5" and "5 cents" are equivalent for a cents question).
               - Classify as "correct" if it matches the correct answer.
               - Classify as "intuitive" if it matches the intuitive (common wrong) answer.
               - Classify as "other" if it gives a different, explicit final answer that
                 matches neither.
               - Classify as "unanswered" if no explicit final answer is present
                 (per rule 3).

            5. Quote the exact substring of candidate_response you used as evidence for
               final_answer. If classification is "unanswered", leave evidence as "".
            
            Return ONLY valid JSON in the following format, nothing else:
            {{
                "final_answer": "...",
                "evidence": "...",
                "classification": "correct|intuitive|other|unanswered"
            }}
            """

        texto = self.llm.generate(prompt, max_tokens=250)

        print("\n_______REPOSTA MODELO BRUTA___________\n")
        print(texto)
        print("\n---------------------------------------\n")

        return converter(texto)

