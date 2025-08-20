# 🐍 Automação em Python - Limpeza e Análise de Dados de Clientes

Este é um projeto simples de **automação em Python**, voltado para
iniciantes, que realiza:
- **Leitura** de uma base de clientes em `.csv`
- **Limpeza** dos dados (remoção de duplicados e valores nulos)
- **Análise exploratória** básica dos dados
- **Geração automática** de um relatório em `.xlsx`

O objetivo é demonstrar como usar **Python + Pandas** para automatizar
tarefas de tratamento de dados.

------------------------------------------------------------------------

## 🚀 Funcionalidades

-   📂 Importa dados de clientes a partir de um arquivo CSV
-   🧹 Remove linhas duplicadas e valores vazios
-   📊 Cria um resumo estatístico das informações
-   🔗 Calcula correlações entre colunas numéricas
-   📑 Exporta os resultados para um relatório em Excel
    (`relatorio_clientes.xlsx`)

------------------------------------------------------------------------

## 🛠️ Tecnologias utilizadas

-   [Python 3]
-   [Pandas]

------------------------------------------------------------------------

## 📂 Estrutura do projeto

    📁 automacao-clientes
     ┣ 📄 base_clientes.csv        # Base de dados de entrada
     ┣ 📄 main.py                  # Script principal do projeto
     ┣ 📄 relatorio_clientes.xlsx  # Relatório gerado automaticamente
     ┗ 📄 README.md                # Documentação do projeto

------------------------------------------------------------------------

## ▶️ Como executar o projeto

1.  **Clonar o repositório**

``` bash
git clone https://github.com/seu-usuario/automacao-clientes.git
cd automacao-clientes
```

2.  **Instalar as dependências**

``` bash
pip install pandas openpyxl
```

3.  **Rodar o script**

``` bash
python main.py
```

4.  O arquivo **`relatorio_clientes.xlsx`** será gerado automaticamente
    com os resultados.

------------------------------------------------------------------------

## 📊 Exemplo de saída no terminal

    Linha iniciais: 1000  - Linhas finais: 950

*(Exemplo fictício -- os números variam conforme a base de clientes
usada.)*

------------------------------------------------------------------------

