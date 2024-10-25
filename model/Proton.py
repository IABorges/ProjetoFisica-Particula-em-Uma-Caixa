import numpy as np
from scipy.integrate import quad

class Proton:
    def __init__(self, largura, n_inicial, n_final):
        self.largura = largura * 1e-9   # largura do poço (em metros)
        self.n_inicial = n_inicial  # nível inicial
        self.n_final = n_final  # nível final
        self.h = 6.62607015e-34  # constante de Planck (J·s)
        self.m = 9.10938356e-31  # massa do **elétron** (kg) -> Correção para massa de elétron
        self.eV = 1.60218e-19  # conversão de energia de elétron-volt para joules (J)

    def funcao_onda(self, n):
        """Calcula a função de onda para um determinado nível."""
        x = np.sqrt(2/self.largura)
        y = (n * np.pi) / self.largura
        return f"ψ(x) = {x:.6f} * sin({y:.6f} * x)"

    def energia(self, n):
        """Calcula a energia no nível n."""
        # Fórmula: E_n = (n^2 * h^2) / (8 * m * L^2)
        return (n**2 * self.h**2) / (8 * self.m * self.largura**2)

    def calcular_energias(self):
        """Calcula as energias dos níveis inicial e final."""
        E_n = self.energia(self.n_inicial)
        E_n2 = self.energia(self.n_final)
        E_nev = E_n / self.eV  # Converte para eV
        E_n2ev = E_n2 / self.eV  # Converte para eV
        return E_n, E_n2, E_nev, E_n2ev

    def velocidade(self, n):
        """Calcula a velocidade da partícula no nível n."""
        return np.sqrt((2 * self.energia(n)) / self.m)
    
    def comprimento_de_broglie(self, n):
        """Calcula o comprimento de onda de De Broglie para um dado nível."""
        p = self.m * self.velocidade(n)  # Momento linear
        return self.h / p  # Comprimento de onda de De Broglie
    

    def funcao_onda_quadrada(self, x, n):
        """Retorna o quadrado da função de onda para um dado nível n."""
        return (2 / self.largura) * np.sin((n * np.pi * x) / self.largura) ** 2

    def calcular_probabilidade(self, x1, x2, n):
        """Calcula a probabilidade de encontrar a partícula entre x1 e x2 no nível n."""
        probabilidade, erro = quad(self.funcao_onda_quadrada, x1, x2, args=(n,))
        return probabilidade * 100  # Converte para porcentagem

       