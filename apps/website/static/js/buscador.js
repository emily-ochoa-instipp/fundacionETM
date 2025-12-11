document.addEventListener("DOMContentLoaded", function () {
    const buscadores = document.querySelectorAll("[data-buscador]");

    buscadores.forEach(buscador => {
        const input = buscador.querySelector("input");
        const tabla = buscador.querySelector("table");
        const filas = tabla.querySelectorAll("tbody tr");
        const mensaje = buscador.querySelector("[data-no-resultados]");

        input.addEventListener("keyup", function () {
            let valor = input.value.toLowerCase();
            let visibles = 0;

            filas.forEach(fila => {
                if (fila.textContent.toLowerCase().includes(valor)) {
                    fila.style.display = "";
                    visibles++;
                } else {
                    fila.style.display = "none";
                }
            });

            mensaje.style.display = visibles === 0 ? "block" : "none";
        });
    });
});
