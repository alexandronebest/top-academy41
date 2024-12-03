
const services = [
    {name: "Услуга 1", description: "Описание услуги 1"},
    {name: "Услуга 2", description: "Описание услуги 2"},
    {name: "Услуга 3", description: "Описание услуги 3"},
];

const servicesList = document.getElementById('services-list');

services.forEach(service => {
    const listItem = document.createElement('li');
    listItem.innerHTML = `<strong>${service.name}</strong>: ${service.description}`;
    servicesList.appendChild(listItem);
});

const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Здесь вы можете обработать отправку данных, например с использованием Fetch API
    console.log(`Имя: ${name}, Email: ${email}, Сообщение: ${message}`);
    alert('Сообщение отправлено!');
    contactForm.reset(); // Сбросить форму
});

function handleScroll() {
    const sections = document.querySelectorAll('section');
    sections.forEach(section => {
        const sectionTop = section.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (sectionTop < windowHeight - 100) {
            section.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', handleScroll);