document.addEventListener('DOMContentLoaded', () => {
    const hamburger = document.querySelector('.navbar-toggler');
    const navbarContent = document.getElementById('navbarNav');

    if (hamburger && navbarContent) {
        hamburger.addEventListener('click', () => {
            navbarContent.classList.toggle('show');
        });
    }
});