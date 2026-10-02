// Utilidades de interfaz. Usar siempre textContent (nunca innerHTML) con datos
// que vengan del usuario o de la API, para evitar ataques XSS.

export function showError(el, mensaje) {
  el.textContent = mensaje;
  el.hidden = false;
}

export function clearError(el) {
  el.textContent = "";
  el.hidden = true;
}

export function setLoading(button, loading, textoCargando = "Procesando...") {
  if (loading) {
    button.dataset.texto = button.textContent;
    button.textContent = textoCargando;
  } else if (button.dataset.texto) {
    button.textContent = button.dataset.texto;
  }
  button.disabled = loading;
}
