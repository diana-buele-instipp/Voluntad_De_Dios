import pytest
pytestmark = pytest.mark.no_db
@pytest.mark.e2e

def test_E2e_login(page, live_server):
    page.goto(live_server.url)

    assert page.url.startswith(live_server.url)
