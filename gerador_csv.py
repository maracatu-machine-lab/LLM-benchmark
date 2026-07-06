import csv

from perguntas import (
    originais_ingles, originais_portugues, originais_espanhol, novas_ingles, novas_portugues, novas_espanhol, originais_ruidos_ingles, originais_ruidos_portugues, originais_ruidos_espanhol,
)

def gerar_csv(nome_arquivo, listas_com_categoria):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['categoria', 'pergunta', 'resposta_correta', 'resposta_intuitiva', 'origem'])
        
        for categoria, lista in listas_com_categoria:
            for p in lista:
                writer.writerow([categoria, p.pergunta, p.resposta_correta, p.resposta_intuitiva, p.origem])

bases_ingles = [
    ('originais', originais_ingles),
    ('novas', novas_ingles),
    ('originais_ruidos_ingles', originais_ruidos_ingles),
]

bases_portugues = [
    ('originais', originais_portugues),
    ('novas', novas_portugues),
    ('originais_ruidos_portugues', originais_ruidos_portugues),
]

bases_espanhol = [
    ('originais', originais_espanhol),
    ('novas', novas_espanhol),
    ('originais_ruidos_espanhol', originais_ruidos_espanhol),
]

gerar_csv('base_ingles.csv', bases_ingles)
gerar_csv('base_portugues.csv', bases_portugues)
gerar_csv('base_espanhol.csv', bases_espanhol)

print("CSVs gerados com sucesso!")