import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_inte_inicio_renderiza_correctamente(client):
    """
    Prueba de integración:
    Verifica que la página de Inicio carga correctamente y contiene
    todos los elementos clave de la interfaz.
    """

    # 1️⃣ Obtener la URL de la vista "inicio"
    url = reverse("inicio")

    # 2️⃣ Realizar la petición GET
    response = client.get(url)

    # 3️⃣ Verificar que la respuesta es correcta
    assert response.status_code == 200

    contenido = response.content.decode()

    # ======= VALIDACIONES DE CONTENIDO =======

    # 4️⃣ Título de la sección
    assert "La consulta incluye" in contenido

    # 5️⃣ Lista de elementos en el cuadro rosado
    assert "Anamnesis detallada" in contenido
    assert "Toma de signos vitales" in contenido
    assert "Medidas antropométricas" in contenido
    assert "Asesoría nutricional" in contenido
    assert "Exploración física completa" in contenido
    assert "Glucosa capilar" in contenido
    assert "Certificado de salud" in contenido

    # 6️⃣ Botones
    assert "Consulta" in contenido
    assert "Consulta Online" in contenido

    # 7️⃣ Imagen del título
    assert "voluntad_dios.png" in contenido

    # 8️⃣ Imagen de la doctora
    assert "doctora.png" in contenido

    # 9️⃣ Elementos provenientes de base.html
    assert "logo_consultorio.png" in contenido     # logo_consultorio del header
    assert "Inicio" in contenido       # menú
    assert "Servicios" in contenido
    assert "Información" in contenido

    # 🔟 Fondo del body (fondo logo rosado)
    assert "fondo_logo.png" in contenido
