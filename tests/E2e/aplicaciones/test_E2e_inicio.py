import pytest
pytestmark = pytest.mark.no_db
@pytest.mark.e2e

def test_pagina_inicio_e2e(page, live_server):
    page.goto(live_server.url)

    assert "Consultorio" in page.content()
    assert "La consulta incluye" in page.content()
