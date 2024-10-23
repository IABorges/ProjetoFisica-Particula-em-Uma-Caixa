import view.PagCalcProton as calcProton
from model.Proton import Proton
from model.Foton import Foton

class Controle:
    def __init__(self, largura, n_inicial, n_final,ponto1,ponto2):
        try:
            self.largura = float(largura)
            self.n_inicial = int(n_inicial)
            self.n_final = int(n_final)
            self.ponto1 = float(ponto1)
            self.ponto2 = float(ponto2)

            if self.largura <= 0:
                raise ValueError("A largura da caixa deve ser positiva.")
            if self.n_inicial <= 0 or self.n_final <= 0:
                raise ValueError("Os níveis devem ser maiores que zero.")

            # Instanciar as classes e calcular
            proton = Proton(self.largura, self.n_inicial, self.n_final,self.ponto1,self.ponto2)
            E_nInicial, E_nFinal, E_nIeV,E_nFJeV = proton.calcular_energias()

            
            print(f"Função de onda nível {self.n_inicial}: {proton.funcao_onda(self.n_inicial)}")
            print(f"Função de onda nível {self.n_final}: {proton.funcao_onda(self.n_final)}")
            print(f"Energia do nível {self.n_inicial}: {E_nInicial:.4e} J ; {E_nIeV:.4f} eV")
            print(f"Energia do nível {self.n_final}: {E_nFinal:.4e} J ; {E_nFJeV:.4f} eV")
            print("-" * 20)
            # Cálculos para o fóton
            foton = Foton(E_nInicial, E_nFinal)
            print(f"Energia do fóton: {foton.energia_foton():.4e} J ; {foton.energia_foton() / 1.60218e-19:.4f} eV")
            print(f"Comprimento de onda do fóton: {foton.comprimento_onda():.4e} m")
            print(f"Frequência do fóton: {foton.frequencia_foton():.4e} Hz")
            print("-" * 100)
            
            print(f"Velocidade da partícula no nível {self.n_inicial}: {proton.velocidade(self.n_inicial):.4e} m/s")
            print(f"Velocidade da partícula no nível {self.n_final}: {proton.velocidade(self.n_final):.4e} m/s")
            print("-" * 100)
            
            print(f"Comprimento de Onda de De Broglie da partícula no nível {self.n_inicial}: {proton.comprimento_de_broglie(self.n_inicial):.4e} m")
            print(f"Comprimento de Onda de De Broglie da partícula no nível {self.n_final}: {proton.comprimento_de_broglie(self.n_final):.4e} m")
            print("-" * 100)

            probabilidade_n_inicial = proton.calc_probabilidade(self.n_inicial, self.ponto1, self.ponto2,self.largura)
            probabilidade_n_final = proton.calc_probabilidade(self.n_final, self.ponto1, self.ponto2,self.largura)

            print(f"Probabilidade no nível {self.n_inicial}: {probabilidade_n_inicial * 100:.2f} %")
            print(f"Probabilidade no nível {self.n_final}: {probabilidade_n_final * 100:.2f} %")

            print(f"integral : {proton.calc_probabilidade(self.n_inicial,self.ponto1,self.ponto2,self.largura) * 100:.2f}")


            
        except ValueError as ve:
            print(f"Erro: {ve}")