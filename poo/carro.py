class Carro:
    def __init__(self, cor, modelo):
        self.cor = cor
        self.modelo = modelo
        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if not self.ligado:
            self.ligado = True
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")

    def desligar(self):
        if self.ligado:
            self.ligado = False
            self.velocidade = 0
            print("O carro foi desligado.")
        else:
            print("O carro já está desligado.")

    def acelerar(self, velocidade):
        if self.ligado:
            self.velocidade += velocidade
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelerar(self, velocidade):
        if self.ligado:
            if self.velocidade >= velocidade:
                self.velocidade -= velocidade
                print(f"O carro desacelerou para {self.velocidade} km/h.")
            else:
                print("O carro já está parado.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

    def imprimir_atributos(self):
        print("Cor:", self.cor)
        print("Modelo:", self.modelo)


meu_carro = Carro(cor="Vermelho", modelo="Toro")
meu_carro.imprimir_atributos()


meu_carro.ligar()


meu_carro.acelerar(73)


meu_carro.desacelerar(11)


meu_carro.desligar()
