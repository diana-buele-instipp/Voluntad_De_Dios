import pytest
from django.urls import reverse
from django.test import Client


@pytest.mark.django_db
def test_login_page_loads_correctly():
    """
    Prueba de integración:
    Verifica que la página de login/inicio cargue correctamente,
    use su template y muestre elementos clave del HTML.
    """

    client = Client()  
    url = reverse('login')  # Asegúrate que tu URL de login tenga name="login"

    response = client.get(url)

    # 1. La página responde correctamente
    assert response.status_code == 200, "❌ El login no carga con 200 OK"

    # 2. Verifica que use el template correcto (si lo tienes en login.html)
    assert "text/html" in response["Content-Type"]

    # 3. Verifica que el contenido esperado esté en la página
    contenido = response.content.decode()

    assert "Voluntad de Dios" in contenido, "❌ No se muestra el título principal"
    assert "La consulta incluye" in contenido, "❌ No aparece la sección de consulta"

    # 4. Verifica que aparecen elementos del menú
    assert "Inicio" in contenido
    assert "Servicios" in contenido
    assert "Información" in contenido

    # 5. Verifica que las imágenes estáticas existan en el HTML
    assert "images/doctora.png" in contenido, "❌ No aparece la imagen de la doctora"
    assert "images/logo.png" in contenido, "❌ No aparece el logo estático"

    print("✅ Prueba de integración del login ejecutada correctamente")
