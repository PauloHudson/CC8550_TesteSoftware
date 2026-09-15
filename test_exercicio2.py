import pytest

from exercicio2 import CarteiraDigital, SaldoInsuficienteError


def test_saque_acima_do_saldo_levanta_excecao():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act e Assert
    with pytest.raises(SaldoInsuficienteError, match="^saldo insuficiente$"):
        carteira.sacar(101)

    # Assert
    assert carteira.saldo == 100


def test_saque_insuficiente_nao_altera_saldo():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    with pytest.raises(SaldoInsuficienteError):
        carteira.sacar(101)

    # Assert
    assert carteira.saldo == 100
