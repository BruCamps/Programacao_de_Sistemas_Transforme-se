lucide.createIcons()

let buttonSubmit = document.querySelector('button'),
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
    function exibeAlertaInputs() {
        paragraphs.forEach(paragraph => {

            totalCaracteres = input.value.length
            inputVazio = totalCaracteres == 0
            paragraphInput = paragraph.id == input.id

            if(!inputVazio && paragraphInput) {
                paragraph.style.display = 'none'
                input.style = 'border: 1.5px solid rgb(201, 201, 201); outline: none;'
            }
        
            if (((input.id == 'nome' || input.id == 'sobrenome') && (totalCaracteres < 3 || inputVazio) && paragraphInput) ||
                (input.id == 'senha' && (totalCaracteres < 8 || inputVazio) && paragraphInput)) {
                paragraph.style = 'display: block; color: #F23D91;'
                input.style = 'border: 1.5px solid transparent; outline: 1px solid #F23D91;'
            }
        })
    }

    input.addEventListener('input', exibeAlertaInputs)
    input.addEventListener('blur', exibeAlertaInputs)
})

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
    if (verificaInput("nome") || verificaInput("sobrenome") || verificaInput("senha")) {
        return false
    } else {    
        return true    
    }
}

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

buttonSubmit.addEventListener('click', (event) => {
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

        exibeModal('Simulação de cadastro feita com sucesso!')

        form.reset()
    }
})

