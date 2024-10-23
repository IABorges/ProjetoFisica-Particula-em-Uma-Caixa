import numpy as np
from scipy.integrate import quad

class Proton:
    def __init__(self, largura, n_inicial, n_final, ponto1, ponto2):
        self.largura = largura  # largura do poço (em metros)
        self.n_inicial = n_inicial  # nível inicial
        self.n_final = n_final  # nível final
        self.pontoInicial = ponto1
        self.pontoFinal = ponto2
        self.h = 6.62607015e-34  # constante de Planck (J·s)
        self.m = 1.6726219e-27  # massa do próton (kg)
        self.eV = 1.60218e-19  # energia de elétron-volt para joules (J)
        self.m = 1.67e-27  # massa do próton em kg

    def funcao_onda(self, n):
        """Calcula a função de onda para um determinado nível."""
        x = np.sqrt(2/self.largura)
        y = (n * np.pi)/self.largura
        #print(f"ψ(x) = {x} * sin({y} * x)")
        return f"ψ(x) = {x} * sin({y} * x)"

    def energia(self, n):
        """Calcula a energia no nível n."""
        return (n**2 * self.h**2) / (8 * self.m * self.largura**2)

    def calcular_energias(self):
        """Calcula as energias dos níveis inicial e final."""
        E_n = self.energia(self.n_inicial)
        E_n2 = self.energia(self.n_final)
        E_nev= E_n/ self.eV
        E_n2ev = E_n2/ self.eV

        return E_n, E_n2, E_nev, E_n2ev
    def velocidade(self,n):
        return np.sqrt((2* self.energia(n))/self.m) 
    
    def comprimento_de_broglie(self,n):
        p = self.m * self.velocidade(n) # momento linear
        return self.h / p  # comprimento de onda
    
    def psi(self,n, x, L):
        return np.sqrt(2 / L) * np.sin(n * np.pi * x / L)

    def calc_probabilidade(self,n, a, b, L):
        # Define a função quadrada da função de onda
        def integrando(x):
            return np.abs(self.psi(n, x, L))**2

        # Calcula a integral
        P, erro = quad(integrando, a, b)
        return P 