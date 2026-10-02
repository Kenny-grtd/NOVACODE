# NOVACODE · Plataforma de Gestión de PQRS

Plataforma web para gestionar **Peticiones, Quejas, Reclamos y Sugerencias (PQRS)** de una empresa pública. Cubre el ciclo completo de una solicitud: **radicación, asignación, resolución y trazabilidad**, con tres perfiles de usuario: ciudadano, funcionario y administrador.

> Este repositorio corresponde a la **segunda versión** del proyecto. La primera versión se desarrolló con Reflex; en esta versión la plataforma se reconstruye con una **API en FastAPI** y despliegue con **Docker**, mejorando la calidad, la seguridad y las funcionalidades.

---

## Tabla de contenido

1. [Objetivos de la versión 2](#objetivos-de-la-versión-2)
2. [Funcionalidades](#funcionalidades)
3. [Roles de usuario](#roles-de-usuario)
4. [Tecnologías](#tecnologías)
5. [Estructura del repositorio](#estructura-del-repositorio)
6. [Puesta en marcha](#puesta-en-marcha)
7. [Variables de entorno](#variables-de-entorno)
8. [Pruebas](#pruebas)
9. [Documentación de la API](#documentación-de-la-api)
10. [Flujo de trabajo con Git](#flujo-de-trabajo-con-git)
11. [Hoja de ruta](#hoja-de-ruta)
12. [Equipo](#equipo)

---

## Objetivos de la versión 2

- Separar el **backend (API REST)** del **frontend** para poder trabajar en paralelo.
- Reforzar la **seguridad**: autenticación con JWT y control de acceso por rol verificado en cada endpoint.
- Implementar una **trazabilidad real** y de solo inserción del historial de cada solicitud.
- Contenerizar la aplicación con **Docker** para que cualquier integrante pueda levantarla con un solo comando.
- Incorporar **pruebas automatizadas** e **integración continua**.
- Agregar nuevas funcionalidades sobre lo construido en la primera versión.

## Funcionalidades

**Heredadas de la versión 1**

- Registro e inicio de sesión de usuarios.
- Radicación de solicitudes con archivos adjuntos y número de radicado.
- Asignación de la solicitud a un área responsable.
- Cambio de estado y respuesta al ciudadano.
- Consulta pública del estado de una solicitud por radicado.
- Notificaciones por correo electrónico.
- Control de plazos de respuesta en días hábiles.
- Reportes y estadísticas, con exportación a Excel/CSV.

**Nuevas en la versión 2**

- Autenticación JWT y permisos por rol.
- Radicado consecutivo y legible.
- Historial de trazabilidad completo por solicitud.
- Reportes calculados únicamente con datos reales.
- Despliegue con Docker Compose.
- Pruebas automatizadas y CI.

<!-- TODO: agregar aquí las funcionalidades nuevas que acuerde el equipo (alertas de vencimiento, comentarios internos, auditoría, etc.) -->

## Roles de usuario

| Rol | Qué puede hacer |
| --- | --- |
| **Ciudadano** | Registrarse, radicar solicitudes, adjuntar documentos, consultar el estado y el historial de sus solicitudes. |
| **Funcionario** | Ver y gestionar solicitudes, asignarlas a un área, cambiar su estado, responderlas y consultar reportes. |
| **Administrador** | Todo lo anterior, además de gestionar usuarios y roles. |

## Tecnologías

| Capa | Tecnología |
| --- | --- |
| Lenguaje | Python 3.12 |
| API | FastAPI + Uvicorn |
| Base de datos | <!-- TODO: confirmar --> PostgreSQL |
| ORM y migraciones | SQLModel / SQLAlchemy + Alembic |
| Autenticación | JWT + bcrypt |
| Pruebas | pytest + httpx |
| Contenedores | Docker + Docker Compose |
| Frontend | <!-- TODO: definir (React / Vue / HTML+JS / Jinja2) --> |
| CI | GitHub Actions |

## Estructura del repositorio

> Estructura objetivo. Puede ajustarse a medida que avance el desarrollo.

```
novacode/
├── backend/
│   ├── app/
│   │   ├── api/routers/      # Endpoints: auth, pqrs, usuarios, reportes
│   │   ├── core/             # Configuración, seguridad, JWT, dependencias de rol
│   │   ├── models/           # Modelos de base de datos
│   │   ├── schemas/          # Esquemas de entrada y salida (Pydantic)
│   │   ├── services/         # Lógica de negocio (radicación, plazos, correos)
│   │   └── main.py
│   ├── alembic/              # Migraciones
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                 # Interfaz de usuario
├── docker-compose.yml
├── .env.example
├── .gitignore
└── README.md
```

## Puesta en marcha

### Requisitos

- [Git](https://git-scm.com/)
- [Docker](https://www.docker.com/) y Docker Compose

### Instalación con Docker

```bash
# 1. Clonar el repositorio
git clone https://github.com/<organizacion-o-usuario>/<nombre-del-repo>.git
cd <nombre-del-repo>

# 2. Crear el archivo de variables de entorno a partir del ejemplo
cp .env.example .env
# Edita .env con tus propios valores

# 3. Construir y levantar los servicios
docker compose up --build
```

Una vez en ejecución:

| Servicio | URL |
| --- | --- |
| API | http://localhost:8000 |
| Documentación interactiva (Swagger) | http://localhost:8000/docs |
| Frontend | <!-- TODO: puerto del frontend --> |

### Ejecución local sin Docker (solo backend)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

## Variables de entorno

Las variables se definen en un archivo `.env` en la raíz del proyecto. **Este archivo nunca debe subirse al repositorio**; solo se versiona `.env.example`, sin valores reales.

| Variable | Descripción |
| --- | --- |
| `DATABASE_URL` | Cadena de conexión a la base de datos. |
| `SECRET_KEY` | Clave para firmar los tokens JWT. |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | Tiempo de vida del token de acceso. |
| `EMAIL_SENDER` | Correo desde el que se envían las notificaciones. |
| `EMAIL_PASSWORD` | Contraseña de aplicación del correo. |
| `SMTP_SERVER` | Servidor SMTP. |
| `SMTP_PORT` | Puerto SMTP. |

<!-- TODO: ajustar la lista cuando se cierre la configuración final -->

## Pruebas

```bash
cd backend
pytest --cov=app
```

## Documentación de la API

FastAPI genera la documentación automáticamente. Con la API en ejecución:

- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

## Flujo de trabajo con Git

### Ramas

| Rama | Uso |
| --- | --- |
| `main` | Código estable y listo para entregar. Protegida: solo se modifica mediante Pull Request. |
| `develop` | Rama de integración donde se unen las funcionalidades. |
| `feature/<nombre>` | Una rama por funcionalidad. Ejemplo: `feature/auth-jwt`. |
| `fix/<nombre>` | Corrección de errores. |

### Mensajes de commit

Se usa el formato [Conventional Commits](https://www.conventionalcommits.org/es/):

```
feat: agrega endpoint de radicación de solicitudes
fix: corrige cálculo de días hábiles
docs: actualiza instrucciones del README
test: agrega pruebas de permisos por rol
refactor: separa la lógica de correos en un servicio
```

### Pull Requests

1. Crear la rama desde `develop`.
2. Hacer commits pequeños y claros.
3. Abrir un Pull Request hacia `develop` describiendo qué cambia y cómo probarlo.
4. Esperar al menos **una revisión** de otro integrante antes de hacer merge.
5. Verificar que las pruebas y el CI pasen.

## Hoja de ruta

- [ ] Configuración del repositorio, ramas y plantillas
- [ ] Estructura base del proyecto con Docker Compose
- [ ] Autenticación JWT y control de acceso por rol
- [ ] Radicación de solicitudes con adjuntos y radicado consecutivo
- [ ] Asignación, cambio de estado y respuesta
- [ ] Trazabilidad e historial de cambios
- [ ] Notificaciones por correo con reintentos
- [ ] Reportes y estadísticas
- [ ] Interfaz de usuario para los tres roles
- [ ] Pruebas automatizadas y CI
- [ ] Documentación final y entrega

## Equipo

**NOVACODE**

| Integrante | Área |
| --- | --- |
| Yeremy Estiven Asprilla Ibargüen | Backend |
| Keni David Espinosa Valencia | Backend |
| Jhan Arinson Sinisterra Garcés | Backend |
| Samuel Cuervo Giraldo | Frontend |
| Ronald Stiven Gamboa Mosquera | Frontend |

---

Proyecto académico desarrollado por el equipo NOVACODE.
