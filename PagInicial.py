import tkinter as tk
from tkinter import messagebox

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
        JanelaInfo(self)  # Passa a instância atual para a nova janela
    def abrir_janela_calcProton(self):
        JanelaCalculoProton(self)
        

# Classe para a segunda janela
class JanelaInfo(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        # Configurações da nova janela
        self.title("Informações")
        self.geometry("500x500")

        # Rótulo com informações adicionais
        labelInfo = tk.Label(self, text="Aqui voce pode ver informações sobre o projeto", font=("Arial", 14))
        labelInfo.pack(pady=20)

        labelIntegrantes = tk.Label(self,text="Integrantes\n -Igor de Araujo Borges; Nº 22.223.006-2\n ",font=("Arial",14))
        labelIntegrantes.pack(pady=20)

        # Botão para fechar a janela
        btnFechar = tk.Button(self, text="Fechar", command=self.destroy)
        btnFechar.pack(pady=10)

class JanelaCalculoProton(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.title("Confinando um Proton")
        self.geometry("800x800")

        labelTitle = tk.Label(self,text="Vamos confinar um Proton:")
        labelTitle.pack(pady=50)

        frameContas = tk.Frame(self)
        frameContas.pack(pady=20)
         # Adicionando labels e entradas para o usuário inserir valores
        tk.Label(frameContas, text="Campo 1:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.entrada1 = tk.Entry(frameContas, width=20)
        self.entrada1.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Campo 2:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10)
        self.entrada2 = tk.Entry(frameContas, width=20)
        self.entrada2.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Campo 3:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        self.entrada3 = tk.Entry(frameContas, width=20)
        self.entrada3.grid(row=2, column=1, padx=10, pady=10)

        # Botão para realizar o cálculo
        btnCalcular = tk.Button(self, text="Calcular", command=self.calcular_proton)
        btnCalcular.pack(pady=20)

    # Função para realizar um cálculo fictício e mostrar uma mensagem
    def calcular_proton(self):
        valor1 = self.entrada1.get()
        valor2 = self.entrada2.get()
        valor3 = self.entrada3.get()

        # Simulação de cálculo simples (você pode modificar conforme necessário)
        resultado = f"Valores inseridos: {valor1}, {valor2}, {valor3}"
        messagebox.showinfo("Resultado", resultado)

# Iniciar a aplicação
if __name__ == "__main__":
    app = JanelaInicio()  # Criar a janela principal
    app.mainloop()        # Iniciar o loop da interface gráfica
