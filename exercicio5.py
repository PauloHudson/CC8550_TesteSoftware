from exercicio2 import CarteiraDigital


def transferir(origem, destino, valor):
    origem.sacar(valor)
    destino.depositar(valor)
