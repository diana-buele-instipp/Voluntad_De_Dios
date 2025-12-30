import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_base_template_render(client):
    response = client.get(reverse("inicio"))
    assert response.status_code == 200
    assert "Consultorio Voluntad de Dios" in response.content.decode()
