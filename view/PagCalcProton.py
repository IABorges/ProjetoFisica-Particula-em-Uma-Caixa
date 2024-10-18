import tkinter as tk
from tkinter import messagebox
import control.Controle
class JanelaCalculoProton(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        global valor1
        self.title("Confinando um Proton")
        self.geometry("800x800")

        labelTitle = tk.Label(self,text="Vamos confinar um Proton:\nDigite as informações que são pedidas por favor!")
        labelTitle.pack(pady=50)

        frameContas = tk.Frame(self)
        frameContas.pack(pady=20)
         # Adicionando labels e entradas para o usuário inserir valores
        tk.Label(frameContas, text="Largura da Caixa", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10)
        self.entrada1 = tk.Entry(frameContas, width=20)
        self.entrada1.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(frameContas,text="Agora voce precisa digitar o estado(n) da particula",font=("Arial",12)).grid(row=1,column=0,padx=10,pady=10)

        tk.Label(frameContas, text="Estado inicial:", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10)
        self.entrada2 = tk.Entry(frameContas, width=20)
        self.entrada2.grid(row=2, column=1, padx=10, pady=10)

        tk.Label(frameContas, text="Estado Final:", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10)
        self.entrada3 = tk.Entry(frameContas, width=20)
        self.entrada3.grid(row=3, column=1, padx=10, pady=10)

        # Botão para realizar o cálculo
        btnCalcular = tk.Button(self, text="Calcular", command=self.calcular_proton)
        btnCalcular.pack(pady=20)

    # Função para realizar um cálculo fictício e mostrar uma mensagem
    def calcular_proton(self):
        valor1 = self.entrada1.get()
        valor2 = self.entrada2.get()
        valor3 = self.entrada3.get()
        # c.test()


        # resultado = f"Valores inseridos: {valor1}, {valor2}, {valor3}"
        # messagebox.showinfo("Resultado", resultado)
    def getValor1():
        return valor1
        