// modal_edicao.js

document.addEventListener("DOMContentLoaded", function () {
  const modal = document.getElementById("modal-edicao");
  const btnEditar = document.getElementById("editarPerfilBtn");
  const btnSalvar = document.getElementById("salvar-edicao");
  const btnCancelar = document.getElementById("cancelar-edicao");

  const campos = {
    nome: document.getElementById("edit-nome"),
    funcao: document.getElementById("edit-funcao"),
    pais: document.getElementById("edit-pais"),
    cidade: document.getElementById("edit-cidade"),
    sobre: document.getElementById("edit-sobre"),
    telefone: document.getElementById("edit-telefone"),
    linkedin: document.getElementById("edit-linkedin"),
    email: document.getElementById("edit-email"),
    github: document.getElementById("edit-github")
  };

  const elementos = {
    nome: document.querySelector(".nome"),
    funcao: document.querySelector(".funcao"),
    pais: document.querySelector(".pais"),
    cidade: document.querySelector(".cidade"),
    sobre: document.querySelector(".sobre_mim"),
    telefone: document.querySelector(".telefone"),
    linkedin: document.querySelector(".linkedin"),
    email: document.querySelector(".email"),
    github: document.querySelector(".github")
  };

  // Abrir modal
  btnEditar.addEventListener("click", () => {
    for (let campo in campos) {
      campos[campo].value = elementos[campo]?.textContent?.trim() || "";
    }
    modal.style.display = "flex";
  });

  // Cancelar
  btnCancelar.addEventListener("click", () => {
    modal.style.display = "none";
  });

  // Salvar e atualizar
  btnSalvar.addEventListener("click", () => {
    for (let campo in campos) {
      if (elementos[campo]) {
        elementos[campo].textContent = campos[campo].value;
      }
    }
    modal.style.display = "none";
    location.reload(); // recarrega a página com os dados atualizados
  });

  // Fechar ao clicar fora
  modal.addEventListener("click", (e) => {
    if (e.target === modal) {
      modal.style.display = "none";
    }
  });
});
