import { logout, requireAuth } from "../auth.js";

const sesion = requireAuth();
if (sesion) {
  const { email, rol, nombres } = sesion.usuario;
  document.getElementById("saludo").textContent = `Hola, ${nombres || email}`;
  document.getElementById("rol").textContent = rol;
  document.getElementById("btn-salir").addEventListener("click", logout);
}
