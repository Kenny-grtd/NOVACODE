# Contrato de la API

Acuerdo entre **backend** y **frontend**. Si algo cambia, se cambia primero aquí (con un Pull Request que revisen ambos equipos) y después en el código.

- Con Docker, el frontend llama a la API en `/api/...` (nginx lo reenvía al backend).
- Con Live Server, el frontend llama a `http://localhost:8000/...`.
- Los endpoints de abajo se escriben **sin** el prefijo `/api`.
- Autenticación: cabecera `Authorization: Bearer <access_token>`.
- Errores: `{"detail": "mensaje"}` (o una lista de `{"msg": ...}` en errores 422).

Estado: ✅ implementado · 🚧 pendiente · 💡 propuesta a acordar.

## Sistema

| Método | Ruta | Descripción | Estado |
| --- | --- | --- | --- |
| GET | `/health` | Estado del servicio | ✅ |
| GET | `/health/db` | Conexión a la base de datos | ✅ |

## Autenticación (Yeremy)

### `POST /auth/registro` 🚧
Registra un ciudadano. Público.

```json
{
  "email": "ana@correo.com",
  "password": "Clave#1234",
  "nombres": "Ana",
  "apellidos": "Pérez",
  "tipo_identificacion": "CC",
  "numero_identificacion": "1234567890",
  "telefono": "3001234567"
}
```
- `201`: `{"id": 1, "email": "ana@correo.com", "rol": "ciudadano"}`
- `409`: `{"detail": "El correo ya está registrado"}`
- `422`: contraseña débil o datos inválidos.

> Los demás campos del registro ampliado de la versión 1 (género, dirección, departamento, ciudad, etnia, persona vulnerable) se agregan después como opcionales.

### `POST /auth/login` 🚧
Público.

```json
{ "email": "ana@correo.com", "password": "Clave#1234" }
```
- `200`:
```json
{
  "access_token": "<jwt>",
  "token_type": "bearer",
  "usuario": { "id": 1, "email": "ana@correo.com", "rol": "ciudadano", "nombres": "Ana" }
}
```
- `401`: `{"detail": "Credenciales inválidas"}`

### `GET /auth/me` 🚧
Requiere token. Devuelve el mismo objeto `usuario` del login.

## Solicitudes PQRS (Keni, Jhan) 💡

Propuesta inicial, a acordar antes de implementarse:

| Método | Ruta | Quién | Descripción |
| --- | --- | --- | --- |
| POST | `/solicitudes` | ciudadano | Radicar una solicitud |
| GET | `/solicitudes` | todos | Lista: el ciudadano ve las suyas; el funcionario, todas (con filtros y paginación) |
| GET | `/solicitudes/{id}` | dueño o funcionario | Detalle con adjuntos |
| GET | `/solicitudes/consulta/{radicado}` | público | Consulta de estado por radicado |
| PATCH | `/solicitudes/{id}/asignar` | funcionario | Asignar área responsable |
| PATCH | `/solicitudes/{id}/estado` | funcionario | Cambiar estado y responder |
| GET | `/solicitudes/{id}/historial` | dueño o funcionario | Trazabilidad |
| GET | `/reportes/resumen` | funcionario | Estadísticas del panel |
| GET | `/usuarios` | administrador | Gestión de usuarios |
| PATCH | `/usuarios/{id}/rol` | administrador | Cambiar rol |
