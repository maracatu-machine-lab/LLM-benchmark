import csv
from pergunta import Pergunta

class GerenciadorPerguntas:
    def __init__(self):
        self.arquivos = {
            'pt': 'base_portugues.csv',
            'en': 'base_ingles.csv',
            'es': 'base_espanhol.csv',
        }
    
        self.configuracoes = [
            {"idioma": "en", "categoria": "originais", "titulo": "Pergunta original - Inglês", "comp": " Give only your final answer.", "id": "ORIG_ING_"},
            {"idioma": "pt", "categoria": "originais", "titulo": "Pergunta original - Português", "comp": " Dê apenas sua resposta final.", "id": "ORIG_POR_"},
            {"idioma": "es", "categoria": "originais", "titulo": "Pergunta original - Espanhol", "comp": " Dame solo tu respuesta final.", "id": "ORIG_ESP_"},
            {"idioma": "en", "categoria": "novas", "titulo": "Pergunta nova - Inglês", "comp": " Give only your final answer.", "id": "NOVA_ING_"},
            {"idioma": "pt", "categoria": "novas", "titulo": "Pergunta nova - Português", "comp": " Dê apenas sua resposta final.", "id": "NOVA_POR_"},
            {"idioma": "es", "categoria": "novas", "titulo": "Pergunta nova - Espanhol", "comp": " Dame solo tu respuesta final.", "id": "NOVA_ESP_"},
            {"idioma": "en", "categoria": "novas_ex", "titulo": "Pergunta nova com exemplo - Inglês", "comp": " Give only your final answer.", "id": "NOVA_EX_ING_"},
            {"idioma": "pt", "categoria": "novas_ex", "titulo": "Pergunta nova com exemplo - Português", "comp": " Dê apenas sua resposta final.", "id": "NOVA_EX_POR_"},
            {"idioma": "es", "categoria": "novas_ex", "titulo": "Pergunta nova com exemplo - Espanhol", "comp": " Dame solo tu respuesta final.", "id": "NOVA_EX_ESP_"},
        ]

    def obter_configuracoes(self):
        return self.configuracoes

    def carregar_lista(self, idioma, categoria=None):
        caminho = self.arquivos.get(idioma)
        if not caminho:
            return []

        perguntas_carregadas = []
        try:
            with open(caminho, mode='r', encoding='utf-8') as f:
                leitor = csv.DictReader(f)
                for linha in leitor:
                    if categoria is None or linha['categoria'] == categoria:
                        p = Pergunta(
                            pergunta=linha['pergunta'],
                            resposta_correta=linha['resposta_correta'],
                            resposta_intuitiva=linha['resposta_intuitiva'],
                            origem=linha['origem']
                        )
                        perguntas_carregadas.append(p)
        except FileNotFoundError:
            print(f"Erro: O arquivo {caminho} não foi encontrado.")
            
        return perguntas_carregadas