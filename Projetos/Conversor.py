import os
import tkinter as tk
from tkinter import filedialog

def criar_exe():
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal do Tkinter

    # Pede ao usuário para selecionar o arquivo Python
    caminho_arquivo_python = filedialog.askopenfilename(
        title="Selecione o arquivo Python",
        filetypes=[("Arquivos Python", "*.py")],
    )

    # Verifica se o usuário cancelou a seleção
    if not caminho_arquivo_python:
        print("Seleção cancelada.")
        return

    # Verifica se o arquivo Python existe
    if not os.path.isfile(caminho_arquivo_python):
        print("Arquivo Python não encontrado.")
        return

    # Cria o executável usando pyinstaller
    os.system(f"pyinstaller --onefile {caminho_arquivo_python}")

    print("Executável criado com sucesso!")

if __name__ == "__main__":
    criar_exe()
