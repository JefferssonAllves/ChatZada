function scrollToSection() {
    const section = document.getElementById('rolagem');
    console.log('veio ate aqui');
    // Scrollar até o final da seção
    section.scrollTo({
        top: section.scrollHeight, // Altura total da seção
        behavior: 'smooth'         // Animação suave
    });
}

document.addEventListener("DOMContentLoaded", function () {
    document.body.classList.add("fade-in");
  });
  
  // Animação de saída ao clicar em links
  const links = document.querySelectorAll("a");
  
  links.forEach(function (link) {
    link.addEventListener("click", function (event) {
      event.preventDefault();
      document.body.classList.remove("fade-in");
      document.body.classList.add("fade-out");
  
      setTimeout(function () {
        window.location.href = link.href;
      }, 500); // Tempo correspondente à transição CSS
    });
  });