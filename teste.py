# Abrir o arquivo para leitura
mercadorias = "mercadorias.txt"
with open(mercadorias, "r", encoding="utf-8") as arquivo:
    #conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    conteudoReadLine = arquivo.readline()
    conteudoReadLines = arquivo.readlines()
# Agora você pode usar 'conteudo' como quiser
print("READ:")
#print(conteudo)
print("READLINE:")
print(conteudoReadLine)
print("READLINES:")
print(conteudoReadLines)