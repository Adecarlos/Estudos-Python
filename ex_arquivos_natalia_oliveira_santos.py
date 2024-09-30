def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            return linhas
    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
        return None

# Função de ler arquivo:
nome_arquivo = "mercadorias.txt"
linhas_arquivo = ler_arquivo(nome_arquivo)

def extrair_itens_e_precos(linhas):
    itens_precos = {}
    for linha in linhas:
        item, preco = linha.strip().split(" = ")
        itens_precos[item] = float(preco)
    return itens_precos

# Vamos testar a função:
itens_precos = extrair_itens_e_precos(linhas_arquivo)

def calcular_media_precos(itens_precos):
    precos = list(itens_precos.values())
    media = sum(precos) / len(precos)
    return media

media_precos = calcular_media_precos(itens_precos)
print(f"Média de preços: R$ {media_precos:.2f}")


item_mais_caro = max(itens_precos, key=itens_precos.get)
item_mais_barato = min(itens_precos, key=itens_precos.get)

print(f"Item mais caro: {item_mais_caro} (custa R$ {itens_precos[item_mais_caro]:.2f})")
print(f"Item mais barato: {item_mais_barato} (custa R$ {itens_precos[item_mais_barato]:.2f})")