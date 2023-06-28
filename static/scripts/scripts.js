// Verifica se há uma posição de rolagem armazenada no local storage
var scrollPosition = localStorage.getItem('scrollPosition');
if (scrollPosition) {
  // Restaura a posição de rolagem
  window.scrollTo(0, scrollPosition);
}

// Armazena a posição de rolagem sempre que houver uma alteração
window.addEventListener('scroll', function () {
  var currentPosition = window.pageYOffset || document.documentElement.scrollTop;
  localStorage.setItem('scrollPosition', currentPosition);
});