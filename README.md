# 📁 Organizador Automático de Arquivos (Python)

Organizador automático de arquivos feito em **Python**, que separa arquivos em pastas por tipo  
(Imagens, Vídeos, Documentos, Áudios, etc.), com foco em **segurança**, **reutilização** e **facilidade de uso**.

---

## ✨ Funcionalidades

- 📂 Organização automática por categoria de arquivo
- 🏗️ Criação automática das pastas necessárias
- 🔁 Pode ser executado várias vezes sem erro
- 🧠 Ignora arquivos temporários (`.tmp`, `.crdownload`)
- 🛡️ Não move arquivos `.py` (segurança)
- 📝 Evita sobrescrever (renomeia automaticamente: `arquivo (1).ext`)
- 📊 Relatório final com total de arquivos organizados
- 🪟 Suporte a versão `.exe` para Windows

---

## 🛠️ Tecnologias utilizadas

- Python 3.9+
- `pathlib`
- `shutil`
- PyInstaller (para gerar o `arquivo.exe`)

---

## ▶️ Como usar (script `.py`)

### 🔹 Requisitos
- Python instalado (versão 3.9 ou superior)

### 🔹 Execução
No terminal, dentro da pasta do projeto:

```bash
python organizador.py
```
---

Ao iniciar, o programa solicitará o caminho da pasta que você deseja organizar.

## 🪟 Como usar no Windows (.exe)

1. Baixe o arquivo organizador.exe na aba Releases

2. Dê duplo clique no executável

3. Informe a pasta que deseja organizar

4. Aguarde a organização e veja o resumo final

5. O .exe funciona mesmo sem Python instalado.

---

## 📌 Categorias suportadas

- Imagens: .jpg, .png, .gif, .webp, .svg, etc.

- Vídeos: .mp4, .mkv, .avi, .mov, etc.

- Documentos: .pdf, .docx, .txt, .md, etc.

- Áudios: .mp3, .wav, .flac, etc.

- Planilhas: .xls, .xlsx, .csv

- Apresentações: .ppt, .pptx

- Executáveis: .exe, .msi, .bat

- Compactados: .zip, .rar, .7z

- Outros: arquivos não identificados

---

## 📂 Exemplo de organização

Antes:

Downloads/
├── foto.jpg
├── video.mp4
├── trabalho.pdf


Depois:

Downloads/
├── Imagens/
│   └── foto.jpg
├── Videos/
│   └── video.mp4
├── Documentos/
│   └── trabalho.pdf

---

## ⚠️ Observações importantes

O programa não apaga arquivos, apenas organiza

Arquivos .py são ignorados por segurança

Arquivos temporários não são movidos

Ideal para pastas como Downloads


---

## 📄 Licença

Projeto de uso livre para fins educacionais e pessoais.

# 👤 Autor

Desenvolvido por Israel Oscar