let menuIcons = document.querySelector('.menu-icon'),
menu = document.querySelector('.navbar ol'),
navbar = document.querySelector('.navbar'),
linksNav = document.querySelectorAll('.navbar li a')

lucide.createIcons()

document.addEventListener('scroll', () => {
    if (window.scrollY > 100) {
        navbar.classList.add('sticky')
    } else {
        navbar.classList.remove('sticky')
    }
})

linksNav.forEach(button => {
    button.addEventListener('click', () => { 
        menuIcons.click() 
    })
})

menuIcons.addEventListener('click', () => {
    menuIcons.classList.toggle('active')
    menu.classList.toggle('active')
})
