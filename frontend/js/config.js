// URL base de la API.
// - Con Docker (http://localhost:3000): nginx reenvía /api/ al backend.
// - Con Live Server (puerto 5500/5501): se llama directo al backend en :8000 (usa CORS).
const puertosDev = ["5500", "5501"];

export const API_BASE = puertosDev.includes(window.location.port)
  ? "http://localhost:8000"
  : "/api";
