from pathlib import Path

import pytest

from exercicio3 import CarteiraDigital


@pytest.fixture
def carteira_com_log(tmp_path):
    log_path = tmp_path / "carteira.log"
    if log_path.exists():
        log_path.unlink()

    carteira = CarteiraDigital(log_path=str(log_path))
    yield carteira

    if log_path.exists():
        log_path.unlink()


def test_deposito_grava_linha_no_log(carteira_com_log):
    # Arrange
    carteira = carteira_com_log

    # Act
    carteira.depositar(75)

    # Assert
    conteudo = Path(carteira.log_path).read_text(encoding="utf-8")
    assert conteudo == "deposito:75\n"
