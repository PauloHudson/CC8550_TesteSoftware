from exercicio1 import CarteiraDigital

#Arrange (preparar): monta os dados e o contexto do teste
#Act (agir): executa a ação que está sendo testada
#Assert (verificar): confere se o resultado é o esperado 

def test_saldo_inicial_zero():
    # Arrange
    carteira = CarteiraDigital()

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 0


def test_saldo_inicial_informado():
    # Arrange
    carteira = CarteiraDigital(150)

    # Act
    saldo = carteira.saldo

    # Assert
    assert saldo == 150


def test_depositar_soma_ao_saldo():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.depositar(50)

    # Assert
    assert carteira.saldo == 150

def test_sacar_subtrai_do_saldo_disponivel():
    # Arrange
    carteira = CarteiraDigital(100)

    # Act
    carteira.sacar(40)

    # Assert
    assert carteira.saldo == 60
