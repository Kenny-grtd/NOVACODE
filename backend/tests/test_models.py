from app.models import EstadoCambio, Rol, Solicitud, Usuario


def test_crear_usuario_y_solicitud_con_historial(session):
    user = Usuario(email="a@b.co", password_hash="hash")
    session.add(user)
    session.commit()
    assert user.rol == Rol.CIUDADANO.value

    sol = Solicitud(
        radicado="PQRS-2026-000001",
        tipo_solicitud="peticion",
        asunto="Prueba",
        descripcion="Descripción",
        usuario_id=user.id,
    )
    session.add(sol)
    session.commit()
    assert sol.estado == "radicada"

    session.add(EstadoCambio(solicitud_id=sol.id, estado_nuevo="radicada"))
    session.commit()
