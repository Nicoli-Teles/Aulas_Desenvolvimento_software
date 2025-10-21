document.addEventListener("DOMContentLoaded", function () {
  const btnAdd = document.getElementById("add-habilidade");
  const lista = document.getElementById("habilidades-lista");

  btnAdd.disabled = false;

  let campoAtivo = null;

  // 🔹 Adiciona botão de remover nas habilidades já existentes
  inicializarBotoesRemover();

  // 🔹 Adicionar nova habilidade
  btnAdd.addEventListener("click", function () {
    // Se já existe um campo ativo, foca nele
    if (campoAtivo !== null) {
      campoAtivo.focus();
      return;
    }

    const wrapper = document.createElement("div");
    wrapper.classList.add("habilidade-item");

    const input = document.createElement("input");
    input.type = "text";
    input.name = "habilidades[]";
    input.placeholder = "Digite uma habilidade e pressione Enter";
    input.classList.add("nova-habilidade");

    const removerBtn = document.createElement("button");
    removerBtn.textContent = "❌";
    removerBtn.classList.add("remover-habilidade");

    // Permite remover e limpa o campoAtivo se for o atual
    removerBtn.addEventListener("click", () => {
      wrapper.remove();
      if (campoAtivo === input) {
        campoAtivo = null;
      }
    });

    wrapper.appendChild(input);
    wrapper.appendChild(removerBtn);
    lista.appendChild(wrapper);

    input.focus();
    campoAtivo = input;

    // Confirmação ao pressionar Enter
    input.addEventListener("keypress", function (event) {
      if (event.key === "Enter") {
        event.preventDefault();
        const texto = input.value.trim();

        if (texto === "") {
          // Se estiver vazio, remove o input e libera campoAtivo
          wrapper.remove();
          campoAtivo = null;
          return;
        }

        input.value = texto;
        input.disabled = true;
        input.classList.remove("nova-habilidade");
        campoAtivo = null;
      }
    });
  });

  // 🔹 Função para adicionar botão "remover" nas habilidades existentes
  function inicializarBotoesRemover() {
    const habilidades = lista.querySelectorAll('input[name="habilidades[]"]');
    habilidades.forEach((input) => {
      // Evita duplicar wrapper se já existir
      if (input.parentNode.classList.contains("habilidade-item")) return;

      const wrapper = document.createElement("div");
      wrapper.classList.add("habilidade-item");

      const removerBtn = document.createElement("button");
      removerBtn.textContent = "❌";
      removerBtn.classList.add("remover-habilidade");

      removerBtn.addEventListener("click", () => {
        wrapper.remove();
        if (campoAtivo === input) campoAtivo = null;
      });

      // move o input existente para dentro do wrapper
      input.parentNode.insertBefore(wrapper, input);
      wrapper.appendChild(input);
      wrapper.appendChild(removerBtn);
    });
  }
});



