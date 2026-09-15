class CarteiraDigital:
    def __init__(self, saldo_inicial=0, log_path="carteira.log"):
        self.saldo = saldo_inicial
        self.log_path = log_path

    def depositar(self, valor):
        self.saldo += valor
        with open(self.log_path, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"deposito:{valor}\n")
