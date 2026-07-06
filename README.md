# 🚀 LLM Pipeline Framework

Um pipeline para execução e avaliação de diferentes modelos de **LLMs (Large Language Models)** com o objetivo de ser um framework, com foco em facilitar pesquisas e benchmarks de **SLMs (Small Language Models)**.

## 🎯 Objetivo

Este projeto fornece um pipeline flexível para:

- 🔄 Executar múltiplos modelos de linguagem
- 📊 Comparar desempenho entre SLMs
- 🧪 Facilitar experimentos e benchmarks
- ⚙️ Padronizar fluxos de avaliação

---

## 🧰 Requisitos

- Python **3.11.8**
- Pip atualizado
- Token do Hugging Face (para download mais rápido de alguns modelos)
    - Logar no Hugging Face
    - Ir para "Access Tokens" -> "Create new token"
    - Selecionar tipo de token "Read", dar um nome ao token e clicar em "Create Token"
    - Copiar o token gerado e salvar para inserir no env do projeto

---

## ⚙️ Setup do Ambiente

Siga os passos abaixo para configurar e executar o ambiente do projeto:

```bash
# Criar ambiente virtual
python -m venv venv

# Ativar ambiente (Windows)
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Criar cópia do ".env.example" e renomear para ".env", alterando a variável "HF_TOKEN" com o valor do token gerado anteriormente

# Executar o código
python main.py

# Para sair do ambiente virtual
deactivate