from pathlib import Path
import shutil

pergunta_caminho = input("Digite o caminho da pasta que deseja organizar: ").strip('"')
PASTA = Path(pergunta_caminho)

if not PASTA.exists() or not PASTA.is_dir():
    print('Caminho inváido, verifique o nome da pasta')
    input('Pressione enter para sair:')
    exit()

CATEGORIAS = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg", ".tiff"],
    "Videos": [".mp4", ".mkv", ".avi", ".m4v", ".mov", ".wmv", ".flv", ".webm"],
    "Documentos": [".pdf", ".doc", ".docx", ".txt", ".md", ".odt", ".rtf"],
    "Compactados": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Executaveis": [".exe", ".msi", ".bat", ".cmd", ".sh"],
    "Audios": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Planilhas": [".xls", ".xlsx", ".csv", ".ods"],
    "Apresentacoes": [".ppt", ".pptx", ".odp"],
    "Codigo": [".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".json", ".xml"],
    "Outros": [],
}

mapa_de_extensoes = {}

for categoria, extensoes in CATEGORIAS.items():
    for ext in extensoes:
        mapa_de_extensoes[ext] = categoria

extensoes_ignoradas = {".tmp", ".crdownload"}

extensoes_puladas = {".py"}

def verificar_extensao(extensao: str) -> str:
    return mapa_de_extensoes.get(extensao, "Outros")

def evitar_repeticao(destino_pasta: Path, item: Path) -> Path:
    caminho_destino = destino_pasta / item.name
    if not caminho_destino.exists():
        return caminho_destino

    base = item.stem
    ext = item.suffix

    contador = 1
    while True:
        novo_nome = f"{base} ({contador}){ext}"
        candidato = destino_pasta / novo_nome
        if not candidato.exists():
            return candidato
        contador += 1


for categoria in CATEGORIAS:
    (PASTA / categoria).mkdir(exist_ok=True)

def organizar_arquivos(PASTA: Path):
    contagem = {categoria: 0 for categoria in CATEGORIAS}
    total_movidos = 0
    ignorados = 0
    pulados = 0 


    for item in PASTA.iterdir():
        if not item.is_file():
            continue

        extensao = item.suffix.lower()

    
        if extensao in extensoes_puladas:
            pulados += 1
            continue

   
        if extensao in extensoes_ignoradas:
            ignorados += 1
            continue

        categoria = verificar_extensao(extensao)
        destino_pasta = PASTA / categoria
        destino_arquivo = evitar_repeticao(destino_pasta, item)

        shutil.move(str(item), str(destino_arquivo))

        contagem[categoria] += 1
        total_movidos += 1

    return contagem, total_movidos, ignorados, pulados
 
def main():
    contagem, total_movidos, ignorados, pulados = organizar_arquivos(PASTA)

    print("\nRESUMO:")
    for categoria, quantidade in contagem.items():
        print(f"{categoria}: {quantidade}")

    print(f"Ignorados (tmp/crdownload): {ignorados}")
    print(f"Pulados (.py): {pulados}")
    print(f"Total de arquivos movidos: {total_movidos}")

    input("\nOrganização concluída! Pressione Enter para sair...")


if __name__ == "__main__":
    main()