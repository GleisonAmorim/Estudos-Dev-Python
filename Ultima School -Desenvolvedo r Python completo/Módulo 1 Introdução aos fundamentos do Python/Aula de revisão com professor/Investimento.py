import tkinter as tk
from tkinter import ttk, messagebox

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        self.style = ttk.Style()
        self.style.configure("TButton", font=('Arial', 14), padding=10)

        self.frame = ttk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.resultado_var = tk.StringVar()
        self.resultado_var.set('')
        
        self.entry_resultado = ttk.Entry(self.frame, textvariable=self.resultado_var, state='disabled', justify='right', font=('Arial', 20))
        self.entry_resultado.grid(row=0, column=0, columnspan=4, pady=5, sticky='nsew')

        self.criar_botoes()

        self.root.bind('<Key>', self.tecla_pressionada)

    def criar_botoes(self):
        botoes = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in botoes:
            btn = ttk.Button(self.frame, text=text, command=lambda t=text: self.clique_botao(t))
            btn.grid(row=row, column=column, sticky='nsew')

        for i in range(5):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(i, weight=1)

    def clique_botao(self, valor):
        if valor == 'C':
            self.resultado_var.set('')
        elif valor == '=':
            try:
                expressao = self.resultado_var.get()
                resultado = eval(expressao)
                self.resultado_var.set(str(resultado))
            except Exception as e:
                messagebox.showerror("Erro", f"Erro na expressão: {e}")
                self.resultado_var.set('')
        else:
            expressao_atual = self.resultado_var.get()
            self.resultado_var.set(expressao_atual + valor)

    def tecla_pressionada(self, event):
        if event.char.isdigit() or event.char in ['+', '-', '*', '/', '=', 'C']:
            self.clique_botao(event.char)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()
