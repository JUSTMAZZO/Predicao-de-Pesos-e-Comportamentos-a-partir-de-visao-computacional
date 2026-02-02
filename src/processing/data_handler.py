import pandas as pd

def carregar_dados_pecuarios(caminho_planilha):
    # Carrega sua planilha (Excel ou CSV)
    try:
        df = pd.read_excel(caminho_planilha) # Ou pd.read_csv
        print("✅ Dados carregados com sucesso!")
        print(df.head()) # Mostra as primeiras linhas
        return df
    except Exception as e:
        print(f"❌ Erro ao carregar: {e}")

# Exemplo de uso
# carregar_dados_pecuarios('data/metadata/sua_planilha.xlsx')