import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_inicio_carga_correctamente(client):
    url = reverse('inicio')
    response = client.get(url)

    assert response.status_code == 200
    assert 'inicio.html' in [t.name for t in response.templates]


@pytest.mark.django_db
def test_inicio_contenido_principal(client):
    response = client.get(reverse('inicio'))

    contenido = response.content.decode()

    # Título / contenido principal
    assert "La consulta incluye" in contenido

    # Botones
    assert "Consulta" in contenido
    assert "Consulta Online" in contenido

    # Imagen doctora
    assert "doctora.png" in contenido

    # Imagen título
    assert "voluntad_dios.png" in contenido
