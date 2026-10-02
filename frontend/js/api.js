import { API_BASE } from "./config.js";
import { getToken, logout } from "./auth.js";

export class ApiError extends Error {
  constructor(status, message) {
    super(message);
    this.status = status;
  }
}

// FastAPI devuelve {detail: "texto"} o {detail: [{msg, loc, ...}]} (errores 422).
function mensajeDeError(detail) {
  if (typeof detail === "string") return detail;
  if (Array.isArray(detail)) return detail.map((d) => d.msg).join(". ");
  return "Ocurrió un error inesperado.";
}

/**
 * Llama a la API. Devuelve el JSON de la respuesta (o null si es 204).
 * Lanza ApiError con un mensaje legible si algo falla.
 *
 *   await apiFetch("/auth/login", { method: "POST", body: {...}, auth: false });
 */
export async function apiFetch(path, { method = "GET", body, auth = true } = {}) {
  const headers = { "Content-Type": "application/json" };
  if (auth) {
    const token = getToken();
    if (token) headers.Authorization = `Bearer ${token}`;
  }

  let res;
  try {
    res = await fetch(`${API_BASE}${path}`, {
      method,
      headers,
      body: body ? JSON.stringify(body) : undefined,
    });
  } catch {
    throw new ApiError(0, "No se pudo conectar con el servidor.");
  }

  if (res.status === 401 && auth) {
    logout(); // token vencido o inválido
    throw new ApiError(401, "Tu sesión expiró. Inicia sesión de nuevo.");
  }
  if (res.status === 204) return null;

  let data = null;
  try {
    data = await res.json();
  } catch {
    /* respuesta sin cuerpo JSON */
  }

  if (!res.ok) throw new ApiError(res.status, mensajeDeError(data?.detail));
  return data;
}
