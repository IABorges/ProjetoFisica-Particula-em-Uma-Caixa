
class Foton:
    def __init__(self, energia_inicial, energia_final):
        self.c = 3e8  # velocidade da luz (m/s)
        self.h = 6.62607015e-34  # constante de Planck (J·s)
        self.energia_inicial = energia_inicial
        self.energia_final = energia_final
        self.eV = 1.60218e-19  # energia de elétron-volt para joules (J)


    def energia_foton(self):    
        """Calcula a energia do fóton absorvido."""
        return (self.energia_final - self.energia_inicial)

    def comprimento_onda(self):
        """Calcula o comprimento de onda do fóton."""
        energia_foton = self.energia_foton()
        return self.h * self.c / energia_foton

    def frequencia_foton(self):
        """Calcula a frequência do fóton."""
        energia_foton = self.energia_foton()
        return energia_foton / self.h