import tkinter as tk
from tkinter import messagebox
import control.Controle as c

class JanelaCalculoProton(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Confinando um Próton")
        self.geometry("600x600")
        self.configure(bg="#f0f0f0")

        # Estilo de fonte padrão
        fonte_titulo = ("Arial", 16, "bold")
        fonte_texto = ("Arial", 12)
        fonte_entrada = ("Arial", 12)
        fonte_botao = ("Arial", 14, "bold")

        # Título da janela
        labelTitle = tk.Label(self, text="Confinando um Próton", font=fonte_titulo, bg="#f0f0f0")
        labelTitle.pack(pady=20)

        # Subtítulo
        subtitle = tk.Label(self, text="Digite as informações necessárias abaixo:", font=fonte_texto, bg="#f0f0f0")
        subtitle.pack(pady=10)

        # Frame para conter os campos de entrada
        frameContas = tk.Frame(self, bg="#f0f0f0")
        frameContas.pack(pady=20)

        # Adicionando labels e entradas para o usuário inserir valores
        tk.Label(frameContas, text="Largura da Caixa (nm):", font=fonte_texto, bg="#f0f0f0").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entrada1 = tk.Entry(frameContas, font=fonte_entrada, width=20)
        self.entrada1.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Estado inicial (n):", font=fonte_texto, bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entrada2 = tk.Entry(frameContas, font=fonte_entrada, width=20)
        self.entrada2.grid(row=1, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Estado final (n):", font=fonte_texto, bg="#f0f0f0").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entrada3 = tk.Entry(frameContas, font=fonte_entrada, width=20)
        self.entrada3.grid(row=2, column=1, padx=10, pady=10)

        # Espaço para cálculo da probabilidade
        tk.Label(frameContas, text="Calcular probabilidade entre dois pontos (nm):", font=fonte_texto, bg="#f0f0f0").grid(row=3, column=0, columnspan=2, pady=20)

        tk.Label(frameContas, text="Ponto 1:", font=fonte_texto, bg="#f0f0f0").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.entrada4 = tk.Entry(frameContas, font=fonte_entrada, width=20)
        self.entrada4.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Ponto 2:", font=fonte_texto, bg="#f0f0f0").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        self.entrada5 = tk.Entry(frameContas, font=fonte_entrada, width=20)
        self.entrada5.grid(row=5, column=1, padx=10, pady=10)

        # Botão para realizar o cálculo
        btnCalcular = tk.Button(self, text="Calcular", font=fonte_botao, bg="#007acc", fg="white", command=self.calcular_proton)
        btnCalcular.pack(pady=30)

        # Estilo adicional do botão ao passar o mouse
        btnCalcular.bind("<Enter>", lambda e: btnCalcular.config(bg="#005f99"))
        btnCalcular.bind("<Leave>", lambda e: btnCalcular.config(bg="#007acc"))

    
        # Função para realizar o cálculo e mostrar o resultado
    def calcular_proton(self):
        try:
            # Pegar os valores das entradas
            largura_caixa = float(self.entrada1.get())  # Largura da caixa em nm
            estado_inicial = int(self.entrada2.get())    # Estado inicial (n)
            estado_final = int(self.entrada3.get())      # Estado final (n)
            ponto1 = float(self.entrada4.get()) * 1e-9  # Converter Ponto 1 de nm para metros
            ponto2 = float(self.entrada5.get()) * 1e-9  # Converter Ponto 2 de nm para metros

            # Instanciar a classe Controle, que internamente usa Proton
            controle = c.Controle(largura_caixa, estado_inicial, estado_final)

            # Calcular a probabilidade para o intervalo e exibir o resultado
           
            for n in range(estado_inicial, estado_final + 1):
                probabilidadcontrole.calcular_probabilidade(ponto1, ponto2, n)
                print(f"Probabilidade no nível {n}: {probabilidade:.2f}%")

          
e = 
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira valores válidos!")
