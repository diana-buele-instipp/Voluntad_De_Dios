import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_inte_informacion_renderiza_correctamente(client):
    """
    Prueba de integración:
    Verifica que la página de Información carga correctamente,
    usa la plantilla base y contiene los elementos principales.
    """

    # 1️⃣ Obtener la URL de la vista "informacion"
    url = reverse("informacion")

    # 2️⃣ Realizar petición GET como un usuario real
    response = client.get(url)

    # 3️⃣ Verificar que la respuesta es correcta (status 200)
    assert response.status_code == 200

    contenido = response.content.decode()

    # 4️⃣ Verifica que se renderiza el título principal
    assert "UBICACIÓN" in contenido

    # 5️⃣ Mapa grande (iframe)
    assert "<iframe" in contenido
    assert "google.com/maps" in contenido

    # 6️⃣ Verifica que aparece la dirección
    assert "Machala San Martín Entre Buenavista y Séptima Este" in contenido

    # 7️⃣ Nombre de la doctora
    assert "Echeverría Loayza Domenica Lilibeth" in contenido

    # 8️⃣ Horario de atención
    assert "Lunes a Viernes" in contenido
    assert "08am a 08pm" in contenido
    assert "Sábado" in contenido
    assert "08am a 04pm" in contenido

    # 9️⃣ Verificar que la imagen de la doctora está en la página
    assert "doctora.png" in contenido

    # 🔟 Asegura que proviene de la plantilla base (logo del header)
    assert "Logo.png" in contenido  

    # 1️⃣1️⃣ Verifica que existen los enlaces del menú
    assert "Inicio" in contenido
    assert "Servicios" in contenido
    assert "Información" in contenido
