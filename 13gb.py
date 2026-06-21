# Gera um arquivo de teste de 13 GB (não é um PDF real)
# Use por sua conta e risco: requer pelo menos 13 GB livres.
tamanho_gb = 13
nome_arquivo = "teste_13GB.bin"

with open(nome_arquivo, "wb") as f:
    bloco = b"\0" * (1024 * 1024)  # 1 MB de zeros
    for _ in range(tamanho_gb * 1024):
        f.write(bloco)

print(f"Arquivo {nome_arquivo} criado com aproximadamente {tamanho_gb} GB.")
