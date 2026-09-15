import pytest

from exercicio2 import SaldoInsuficienteError
from exercicio5 import CarteiraDigital, transferir


@pytest.fixture
def carteiras():
    return CarteiraDigital(100), CarteiraDigital()


@pytest.mark.parametrize(
    "valor",
    [
        pytest.param(10, id="transferencia-pequena"),
        pytest.param(50, id="transferencia-media"),
        pytest.param(100, id="transferencia-do-saldo-total"),
    ],
)
def test_transferencia_bem_sucedida(carteiras, valor):
    # Arrange
    origem, destino = carteiras
    saldo_inicial_da_origem = origem.saldo

    # Act
    transferir(origem, destino, valor)

    # Assert
    assert origem.saldo == saldo_inicial_da_origem - valor
    assert destino.saldo == valor


def test_transferencia_insuficiente_nao_altera_as_carteiras(carteiras):
    # Arrange
    origem, destino = carteiras
    saldo_inicial_da_origem = origem.saldo
    saldo_inicial_do_destino = destino.saldo

    # Act
    with pytest.raises(SaldoInsuficienteError):
        transferir(origem, destino, saldo_inicial_da_origem + 1)

    # Assert
    assert origem.saldo == saldo_inicial_da_origem
    assert destino.saldo == saldo_inicial_do_destino
