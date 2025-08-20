import pandas as pd

tabela = pd.read_csv("base_clientes.csv")

linhas_iniciais = len(tabela)

# Limpeza de valores duplicados
tabela = tabela.drop_duplicates()

# Limpeza de valores vazios
tabela = tabela.dropna()

linhas_finais = len(tabela)

print("Linha iniciais:", linhas_iniciais, " - Linhas finais:", linhas_finais)

# Exploração de dados
resumo = tabela.describe(include="all")
correlacoes = tabela.corr(numeric_only=True)

# Exportando os resultados
with pd.ExcelWriter("relatorio_clientes.xlsx") as arquivo:
    resumo.to_excel(arquivo, sheet_name="Resumo de Dados")
    correlacoes.to_excel(arquivo, sheet_name="Correlação")