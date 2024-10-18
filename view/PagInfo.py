# Classe para a segunda janela

import tkinter as tk
from tkinter import messagebox

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