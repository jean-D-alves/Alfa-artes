function enviarmensagem(texto) {
    const numero = 5584996153922
    const mensagem = encodeURIComponent(texto)
    const link = 'https://wa.me/${numero}?text=${mensagem}'
    window.open(link, "_blank")
}
