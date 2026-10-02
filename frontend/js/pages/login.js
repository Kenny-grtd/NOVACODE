import { apiFetch } from "../api.js";
import { getSession, redirectByRole, saveSession } from "../auth.js";
import { clearError, setLoading, showError } from "../ui.js";

const sesion = getSession();
if (sesion) redirectByRole(sesion.usuario.rol);

const form = document.getElementById("form-login");
const error = document.getElementById("error");
const boton = form.querySelector("button[type=submit]");

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  clearError(error);

  const email = form.email.value.trim();
  const password = form.password.value;
  if (!email || !password) {
    showError(error, "Ingresa tu correo y tu contraseña.");
    return;
  }

  setLoading(boton, true, "Ingresando...");
  try {
    const data = await apiFetch("/auth/login", {
      method: "POST",
      body: { email, password },
      auth: false,
    });
    saveSession(data);
    redirectByRole(data.usuario.rol);
  } catch (err) {
    showError(error, err.message);
    setLoading(boton, false);
  }
});
