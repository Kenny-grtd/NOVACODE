# Frontend · NOVACODE

HTML + CSS + JavaScript (módulos ES). Sin frameworks ni paso de compilación.

## Cómo ejecutarlo

**Opción A: con Docker** (la misma que usará la entrega)

```bash
docker compose up --build
```
Abrir http://localhost:3000. nginx sirve el frontend y reenvía `/api/` al backend.

**Opción B: Live Server de VS Code** (más cómodo para diseñar)

1. Levantar solo el backend: `docker compose up --build api db`
2. En VS Code, clic derecho en `frontend/index.html` → *Open with Live Server* (puerto 5500).

> Los módulos ES no funcionan abriendo el archivo con doble clic (`file://`); hay que usar un servidor.

## Estructura

```
frontend/
├── index.html, login.html, registro.html, panel.html
├── css/styles.css        # variables de color y estilos base
└── js/
    ├── config.js         # URL base de la API
    ├── api.js            # apiFetch(): llamadas a la API con token y errores
    ├── auth.js           # sesión, requireAuth(), redirecciones por rol
    ├── ui.js             # showError, clearError, setLoading
    └── pages/            # un archivo JS por página
```

## Cómo agregar una página nueva

1. Crear `mipagina.html` copiando la estructura de `login.html`.
2. Crear `js/pages/mipagina.js`, importar lo necesario y enlazarlo con `<script type="module">`.
3. Si la página es privada, empezar con `const sesion = requireAuth(["funcionario"]);`.
4. Llamar a la API solo con `apiFetch(...)`, siguiendo `docs/contrato-api.md`.

## Reglas del equipo

- **Nunca `innerHTML` con datos de usuarios o de la API**; usar `textContent`. Evita ataques XSS.
- Validar en el navegador es solo comodidad: el backend siempre vuelve a validar.
- Ocultar un botón por rol no protege nada; el permiso real lo da la API.
- Un campo = un `<label>` asociado. Los errores van en un elemento con `role="alert"`.
- Probar en pantalla de celular (el CSS ya es responsivo).
- Pendiente: el token se guarda en `localStorage`. Es aceptable para este proyecto, pero conviene mencionar en la entrega que en producción se preferiría una cookie `HttpOnly`.
