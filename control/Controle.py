import view.PagCalcProton as calcProton

class Controle():

    def __init__(self,largura,nInicial,nFinal):
        self.largura = float(largura)
        self.n_inicial = int(nInicial)
        self.n_final = int(nFinal)

        try:
        # Verifica se os valores são válidos
            if self.largura <= 0:
                raise ValueError("A largura da caixa deve ser um valor positivo.")
            if self.n_inicial <= 0 or self.n_final <= 0:
                raise ValueError("Os estados da partícula devem ser maiores que zero.")

                # Aqui, você pode fazer o cálculo ou chamar a função que realiza o cálculo
            #resultado = self.calcular_confinamento(self.largura, self.n_inicial, self.n_final)
            resultado = self.largura + self.n_final + self.n_inicial
            print(resultado)
           # return f"Resultado do cálculo: {resultado}"

        except ValueError as ve:
            # Retorna uma mensagem de erro se houver problemas com os dados inseridos
            #return f"Erro de valor: {ve}"
            print("erro")
