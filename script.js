// script.js
function toggleMenu() {
    const menu = document.querySelector('.main-nav ul');
    const hamburger = document.querySelector('.hamburger');
    menu.classList.toggle('open');
    hamburger.classList.toggle('active');
}

// Close the menu when a link is clicked
document.querySelectorAll('.main-nav a').forEach(link => {
    link.addEventListener('click', () => {
        document.querySelector('.main-nav ul').classList.remove('open');
        document.querySelector('.hamburger').classList.remove('active');
    });
});
