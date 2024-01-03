import requests
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class HTMLDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Downloader")

        self.create_widgets()

    def create_widgets(self):
        # Rótulo e campo de entrada para a URL
        ttk.Label(self.root, text="URL da Página:").grid(row=0, column=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(self.root, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        # Botão para iniciar o download
        download_button = ttk.Button(self.root, text="Baixar HTML", command=self.download_html)
        download_button.grid(row=1, column=0, columnspan=2, pady=10)

    def download_html(self):
        # Obtém a URL inserida
        url = self.url_entry.get()

        if not url:
            messagebox.showwarning("Aviso", "Por favor, insira uma URL.")
            return

        try:
            # Faz a solicitação GET à URL
            response = requests.get(url)

            # Verifica se a solicitação foi bem-sucedida (código de status 200)
            if response.status_code == 200:
                # Salva o conteúdo HTML em um arquivo
                with open("pagina.html", "w", encoding="utf-8") as file:
                    file.write(response.text)
                messagebox.showinfo("Download Concluído", "O HTML foi baixado com sucesso!")
            else:
                # Se a solicitação não for bem-sucedida, mostra uma mensagem de erro
                messagebox.showerror("Erro", f"Falha no download. Código de status: {response.status_code}")
        except Exception as e:
            # Mostra uma mensagem de erro se ocorrer uma exceção
            messagebox.showerror("Erro", f"Falha no download. {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HTMLDownloaderApp(root)
    root.mainloop()