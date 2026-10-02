// Manejo de sesión en el navegador.
// IMPORTANTE: estas validaciones son solo de experiencia de usuario.
// La seguridad real (roles, permisos) la aplica siempre el backend.

const KEY = "novacode_session";

// Página de inicio por rol. Cambiar cuando existan los paneles reales.
const HOME_BY_ROLE = {
  ciudadano: "panel.html",
  funcionario: "panel.html",
  administrador: "panel.html",
};

export function saveSession(data) {
  localStorage.setItem(
    KEY,
    JSON.stringify({ token: data.access_token, usuario: data.usuario }),
  );
}

export function getSession() {
  try {
    return JSON.parse(localStorage.getItem(KEY));
  } catch {
    return null;
  }
}

export function getToken() {
  return getSession()?.token ?? null;
}

export function logout() {
  localStorage.removeItem(KEY);
  window.location.href = "login.html";
}

export function redirectByRole(rol) {
  window.location.href = HOME_BY_ROLE[rol] ?? "panel.html";
}

/** Exige sesión (y opcionalmente un rol). Devuelve la sesión o redirige. */
export function requireAuth(roles = null) {
  const session = getSession();
  if (!session) {
    window.location.href = "login.html";
    return null;
  }
  if (roles && !roles.includes(session.usuario.rol)) {
    window.location.href = "panel.html";
    return null;
  }
  return session;
}
