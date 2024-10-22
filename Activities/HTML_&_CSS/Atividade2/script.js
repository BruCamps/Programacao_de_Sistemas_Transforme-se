lucide.createIcons()

let buttonElement = document.querySelector('button'),
    checkboxes = document.querySelectorAll('.content-checkboxers input'),
    radios = document.querySelectorAll('.content-radios input'),
    inputs = document.querySelectorAll('.content-texts input'),
    paragraphs = document.querySelectorAll('.content-texts p')

const form = document.getElementById('form'),
    Modalcontainer = document.getElementById('alert'),
    msgModal = document.getElementById('alert-message'),
    triangleIcon = document.getElementById('triangle-alert'),
    badgeIcon = document.getElementById('badge-check'),
    closeBtn = document.querySelector('.close-button'),
    confirmBtn = document.getElementById('alert-confirm')

inputs.forEach(input => {

    input.addEventListener('input', () => {

        paragraphs.forEach(paragraph => {

            if(paragraph.id == input.id && (input.value.length >= 3 || input.value.length == 0)) {
                paragraph.style.display = 'none'
                input.style.border = 'none'
            }
            
            if ((input.id == 'nome' || input.id == 'sobrenome') && (input.value.length < 3 && input.value.length != 0 && paragraph.id == input.id)) {
                paragraph.style.display = 'block'
                input.style.border = '1px solid #F23D91'
            }
            
            if (input.id == 'senha' && (input.value.length < 8 && input.value.length != 0 && paragraph.id == input.id)) {
                paragraph.style.display = 'block'
                input.style.border = '1px solid #F23D91'
            }
        })

    })
})
function exibeModal(message) {
    msgModal.textContent = message
    Modalcontainer.style.display = 'flex'
    
    function fechaModal() {
        Modalcontainer.style.display = 'none'
    }
    
    confirmBtn.addEventListener('click', fechaModal)
    closeBtn.addEventListener('click', fechaModal)
    
    window.addEventListener('click', event => {
        if (event.target === Modalcontainer) {
            fechaModal()
        }
    })
}
function verificaInput(id) {
    var field = document.getElementById(id).value

    if (id == 'nome' || id == 'sobrenome') {
        return field.length < 3
    } 
    if (id == 'senha') {
        return field.length < 8
    }
}

function validaInputs() {
    if (
        verificaInput("nome")  || 
        verificaInput("sobrenome") || 
        verificaInput("senha")
    ) {
        return false
    } else {    
        return true    
    }
}

buttonElement.addEventListener('click', (event) => {
    let checkboxesVazias = !checkboxes[0].checked && !checkboxes[1].checked && !checkboxes[2].checked && !checkboxes[3].checked,
        radiosVazios = !radios[0].checked && !radios[1].checked && !radios[2].checked
        
    event.preventDefault()

    if (checkboxesVazias || radiosVazios || !validaInputs()) {
        triangleIcon.style.display = 'block'
        badgeIcon.style.display = 'none'
        exibeModal('Todos os campos devem ser preenchidos!')
    }

    if (!checkboxesVazias && !radiosVazios && validaInputs()) {
        triangleIcon.style.display = 'none'
        badgeIcon.style.display = 'block'
        exibeModal('Simulação de cadastrado feita com sucesso!')
        form.reset()
    }
})

