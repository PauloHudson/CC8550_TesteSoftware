import pytest

from exercicio4 import classificar_transacao


# Falha identificada: usando <= 100, o valor 100 era classificado como
# "pequena"; usando <= 1000, o valor 1000 era classificado como "media".
# A funcao foi corrigida usando <, deixando 100 como "media" e 1000 como "grande".
@pytest.mark.parametrize(
    ("valor", "categoria"),
    [
        pytest.param(0, "pequena", id="zero-pequena"),
        pytest.param(99, "pequena", id="abaixo-de-cem"),
        pytest.param(100, "media", id="cem-media"),
        pytest.param(999, "media", id="abaixo-de-mil"),
        pytest.param(1000, "grande", id="mil-grande"),
        pytest.param(1500, "grande", id="acima-de-mil"),
    ],
)

def test_classifica_transacao_nos_limites(valor, categoria):
    # Arrange
    valor_da_transacao = valor

    # Act
    resultado = classificar_transacao(valor_da_transacao)

    # Assert
    assert resultado == categoria
