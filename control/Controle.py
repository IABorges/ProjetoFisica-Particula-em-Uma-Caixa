import view.PagCalcProton as calcProton
from model.Proton import Proton
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

            # # Cálculos para o fóton
            # fotao = Fotao(E_n3, E_n4)
            # print(f"Energia do fóton: {fotao.energia_foton()} J")
            # print(f"Comprimento de onda do fóton: {fotao.comprimento_onda()} m")
            # print(f"Frequência do fóton: {fotao.frequencia_foton()} Hz")

        except ValueError as ve:
            print(f"Erro: {ve}")