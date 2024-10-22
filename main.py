import tkinter as tk
from tkinter import messagebox
import view.PagInfo as pInfo
import view.PagCalcProton as calcProton

# Classe para a janela principal
class JanelaInicio(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela principal
        self.title("Início")
        self.geometry("500x500")

        # Criando o frame principal
        frameMain = tk.Frame(self)
        frameMain.pack(fill="both", expand=True)

        # Rótulo com o texto explicativo
        labelInfo1 = tk.Label(frameMain, text="Bem-vindo ao projeto de física.\nEle faz muitas coisas interessantes.", 
                              font=("Arial", 16), wraplength=400)
        labelInfo1.grid(padx=20, pady=40, row=0, column=0, columnspan=2)

        # Definindo os botões com o mesmo tamanho
        button_width = 25  
        button_height = 2

        # Botão 1
        btnBotao1 = tk.Button(frameMain, text="Confinar o elétron", width=button_width, height=button_height)
        btnBotao1.grid(row=1, column=0, padx=20, pady=20, sticky="e")

        # Botão 2
        btnBotao2 = tk.Button(frameMain, text="Confinar o próton", width=button_width, height=button_height,command=self.abrir_janela_calcProton)
        btnBotao2.grid(row=1, column=1, padx=20, pady=20, sticky="w")

        # Botão para abrir a nova janela
        btnBotaoInfo = tk.Button(frameMain, text="Informações", width=button_width, height=button_height, command=self.abrir_janela_info)
        btnBotaoInfo.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    # Método para abrir a nova janela
    def abrir_janela_info(self):
       pInfo.JanelaInfo(self)  # Passa a instância atual para a nova janela
    def abrir_janela_calcProton(self):
        calcProton.JanelaCalculoProton(self)
        

# Iniciar a aplicação
if __name__ == "__main__":
    app = JanelaInicio()  # Criar a janela principal
    app.mainloop()        # Iniciar o loop da interface gráfica
