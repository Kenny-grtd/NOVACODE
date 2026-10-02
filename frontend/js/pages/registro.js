import { apiFetch } from "../api.js";
import { clearError, setLoading, showError } from "../ui.js";

const form = document.getElementById("form-registro");
const error = document.getElementById("error");
const exito = document.getElementById("exito");
const boton = form.querySelector("button[type=submit]");

// Misma regla que la versión 1: 8+ caracteres, mayúscula, minúscula, número y símbolo.
// El backend vuelve a validarla; esto solo da retroalimentación rápida.
function passwordValida(p) {
  return (
    p.length >= 8 &&
    /[A-Z]/.test(p) &&
    /[a-z]/.test(p) &&
    /\d/.test(p) &&
    /[^A-Za-z0-9]/.test(p)
  );
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearError(error);
  exito.hidden = true;

  const f = form.elements;
  if (!form.checkValidity()) {
    showError(error, "Completa todos los campos obligatorios.");
    return;
  }
  if (!passwordValida(f.password.value)) {
    showError(
      error,
      "La contraseña debe tener mínimo 8 caracteres, con mayúscula, minúscula, número y símbolo.",
    );
    return;
  }
  if (f.password.value !== f.confirmar.value) {
    showError(error, "Las contraseñas no coinciden.");
    return;
  }

  setLoading(boton, true, "Registrando...");
  try {
    await apiFetch("/auth/registro", {
      method: "POST",
      auth: false,
      body: {
        email: f.email.value.trim(),
        password: f.password.value,
        nombres: f.nombres.value.trim(),
        apellidos: f.apellidos.value.trim(),
        tipo_identificacion: f.tipo_identificacion.value,
        numero_identificacion: f.numero_identificacion.value.trim(),
        telefono: f.telefono.value.trim() || null,
      },
    });
    form.reset();
    exito.hidden = false;
  } catch (err) {
    showError(error, err.message);
  } finally {
    setLoading(boton, false);
  }
});
