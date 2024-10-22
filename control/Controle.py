import view.PagCalcProton as calcProton
from model.Proton import Proton
from model.Foton import Foton
class Controle:
    def __init__(self, largura, n_inicial, n_final):
        try:
            self.largura = float(largura)
            self.n_inicial = int(n_inicial)
            self.n_final = int(n_final)

            if self.largura <= 0:
                raise ValueError("A largura da caixa deve ser positiva.")
            if self.n_inicial <= 0 or self.n_final <= 0:
                raise ValueError("Os níveis devem ser maiores que zero.")

            # Instanciar as classes e calcular
            proton = Proton(self.largura, self.n_inicial, self.n_final)
            E_nInicial, E_nFinal, E_nIeV,E_nFJeV = proton.calcular_energias()

            print(f"Função de onda nível {self.n_inicial}: {proton.funcao_onda(self.n_inicial)}")
            print(f"Função de onda nível {self.n_final}: {proton.funcao_onda(self.n_final)}")
            print(f"Energia do nível {self.n_inicial}: {E_nInicial} J ; {E_nIeV} eV")
            print(f"Energia do nível {self.n_final}: {E_nFinal} J ; {E_nFJeV} eV")
            print("-"*20)
            # Cálculos para o fóton
            foton = Foton(E_nInicial, E_nFinal)
            print(f"Energia do fóton: {foton.energia_foton()} J : {foton.energia_foton()/ 1.60218e-19 } eV")
            print(f"Comprimento de onda do fóton: {foton.comprimento_onda()} m")
            print(f"Frequência do fóton: {foton.frequencia_foton()} Hz")
            print("-"*100)
            print(f"Velocidade da particula no nivel {self.n_inicial}: {proton.velocidade(self.n_inicial)} m/s")
            print(f"Velocidade da particula no nivel {self.n_final}: {proton.velocidade(self.n_final)} m/s")
            print("-"*100)
            print(f"Comprimento de Onda de De Broglie da particula no nivel {self.n_inicial}: {proton.comprimento_de_broglie(self.n_inicial)} m ")
            print(f"Comprimento de Onda de De Broglie da particula no nivel {self.n_final}: {proton.comprimento_de_broglie(self.n_final)} m ")
            print("-"*100)
            
        except ValueError as ve:
            print(f"Erro: {ve}")