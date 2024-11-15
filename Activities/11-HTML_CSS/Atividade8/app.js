var listNavbar = document.querySelector('.nav ol'),
itemNavbar = document.querySelectorAll('.nav ol li'),
menuIcon = document.querySelector('.menu-icon');

itemNavbar.forEach(item => {
    item.addEventListener('click', function() {
        menuIcon.click();
    })
})

menuIcon.addEventListener('click', function() {
    listNavbar.classList.toggle('active');
})