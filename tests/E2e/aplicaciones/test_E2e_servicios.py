import pytest
pytestmark = pytest.mark.no_db
@pytest.mark.e2e

def test_E2e_servicios(page, live_server):
    page.goto(live_server.url + "/servicios/")

    contenido = page.content()
    assert "Servicios" in contenido
