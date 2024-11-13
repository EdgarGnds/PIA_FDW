function mostrarInformacion() {
                
    let carta = prompt("¿Cuál es tu carta favorita de Clash Royale?");
    
    if (carta === null || carta.trim() === "") {
        alert("No ingresaste una carta. Inténtalo de nuevo.");
        return;  
    }

    carta = carta.toLowerCase();

    let informacionCarta;

    if (carta === "montapuercos") {
        informacionCarta = "Montapuercos es una carta de 4 de elixir que se utiliza para atacar directamente las torres enemigas.";
    } else if (carta === "princesa") {
        informacionCarta = "Princesa es una carta legendaria de 3 de elixir que dispara flechas desde una gran distancia.";
    } else if (carta === "esqueletos") {
        informacionCarta = "Esqueletos es una carta de 1 de elixir que invoca 3 pequeños esqueletos. Son útiles para distraer.";
    } else {
        informacionCarta = `No tenemos información sobre la carta "${carta}". Intenta con otra.`;
    }

    alert(informacionCarta);
    document.getElementById("resultado").innerText = informacionCarta;
}