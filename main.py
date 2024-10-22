import tkinter as tk
from tkinter import messagebox
import view.PagInfo as pInfo
import view.PagCalcProton as calcProton

# Classe para a janela principal
class JanelaInicio(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Início - Projeto de Física")
        self.geometry("700x500")
        self.configure(bg="#f0f0f0")

        # Criando o frame principal
        frameMain = tk.Frame(self, bg="#f0f0f0")
        frameMain.pack(fill="both", expand=True, pady=50, padx=20)

        # Rótulo com o texto explicativo
        labelInfo1 = tk.Label(frameMain, 
                              text="Bem-vindo ao projeto de física.\nEste programa permite confinar partículas e realizar cálculos físicos interessantes.",
                              font=("Arial", 16, "bold"), wraplength=450, bg="#f0f0f0", justify="center")
        labelInfo1.grid(pady=40, row=0, column=0, columnspan=2)

        # Definindo os botões com o mesmo tamanho e estilo
        button_width = 25  
        button_height = 2
        fonte_botao = ("Arial", 14, "bold")

        # Botão 1 - Confinar o elétron
        btnBotao1 = tk.Button(frameMain, text="Confinar o elétron", width=button_width, height=button_height,
                              font=fonte_botao, bg="#007acc", fg="white")
        btnBotao1.grid(row=1, column=0, padx=20, pady=20, sticky="e")

        # Estilo do botão ao passar o mouse
        btnBotao1.bind("<Enter>", lambda e: btnBotao1.config(bg="#005f99"))
        btnBotao1.bind("<Leave>", lambda e: btnBotao1.config(bg="#007acc"))

        # Botão 2 - Confinar o próton
        btnBotao2 = tk.Button(frameMain, text="Confinar o próton", width=button_width, height=button_height,
                              font=fonte_botao, bg="#007acc", fg="white", command=self.abrir_janela_calcProton)
        btnBotao2.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Estilo do botão ao passar o mouse
        btnBotao2.bind("<Enter>", lambda e: btnBotao2.config(bg="#005f99"))
        btnBotao2.bind("<Leave>", lambda e: btnBotao2.config(bg="#007acc"))

        # Botão para abrir a janela de informações
        btnBotaoInfo = tk.Button(frameMain, text="Informações", width=button_width, height=button_height,
                                 font=fonte_botao, bg="#007acc", fg="white", command=self.abrir_janela_info)
        btnBotaoInfo.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

        # Estilo do botão ao passar o mouse
        btnBotaoInfo.bind("<Enter>", lambda e: btnBotaoInfo.config(bg="#005f99"))
        btnBotaoInfo.bind("<Leave>", lambda e: btnBotaoInfo.config(bg="#007acc"))

    # Método para abrir a janela de informações
    def abrir_janela_info(self):
        pInfo.JanelaInfo(self)  # Passa a instância atual para a nova janela
    
    # Método para abrir a janela de cálculo do próton
    def abrir_janela_calcProton(self):
        calcProton.JanelaCalculoProton(self)

# Iniciar a aplicação
if __name__ == "__main__":
    app = JanelaInicio()  # Criar a janela principal
    app.mainloop()        # Iniciar o loop da interface gráfica
