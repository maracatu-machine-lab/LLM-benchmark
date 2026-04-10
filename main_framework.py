from factory import load_model
import concurrent.futures

def generate_text():
    return llm.generate(prompt)


if __name__ == "__main__":
    print('Início')

    # TROCA AQUI
    llm = load_model("clinical")

    prompt = "Explique hipertensão arterial em duas linhas."

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(generate_text)
        try:
            timeout_in_seconds = 600
            response = future.result(timeout= timeout_in_seconds) # 5 minutos
            print("\nResposta:\n")
            print(response)
        except concurrent.futures.TimeoutError:
            print("Tempo limite de geração excedido!")