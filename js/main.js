const hamburger = document.querySelector(".hamburger");
const mobileMenu = document.querySelector(".mobile");

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("toggle");
  mobileMenu.classList.toggle("nav-open");
});
