lucide.createIcons()

let inputs = document.querySelectorAll('form .campo'),
    paragraphs = document.querySelectorAll('form .alert-msg'),
    checkboxes = document.querySelectorAll('.content-checkboxers input'),
    radios = document.querySelectorAll('.content-radios input'),
    buttonReset = document.querySelector('button[type="reset"]'),
    buttonSubmit = document.querySelector('button[type="submit"]')

const form = document.getElementById('form'),
    Modalcontainer = document.getElementById('alert'),
    msgModal = document.getElementById('alert-message'),
    triangleIcon = document.getElementById('triangle-alert'),
    badgeIcon = document.getElementById('badge-check'),
    closeBtn = document.querySelector('.close-button'),
    confirmBtn = document.getElementById('alert-confirm')
    
inputs.forEach(input => {
    function exibeAlertaInputs(){

        paragraphs.forEach(paragraph => {

            inputVazio = input.value.length == 0
            paragraphInput = paragraph.id == input.id

            if(input.id == 'outros-filmes' && !inputVazio && paragraphInput) {
                paragraph.style.display = 'none'
                input.classList.remove('required')
            }

            if(input.id == 'idade') {
                input.value = input.value.replace('-', '')
                idade = Number(input.value)

                if(idade < 1 || idade > 100) {
                    input.value = input.value.slice(0, -1)
                }
            }
            
            if (paragraphInput && !inputVazio && input.id != 'outros-filmes') {
                paragraph.style.display = 'none'
                input.style.outline = 'none'
                input.style.border = '1.5px solid rgb(201, 201, 201)'
            }

            if ((input.id == 'nome' || input.id == 'idade' || (input.id == 'outros-filmes' && checkboxes[4].checked && input.classList.contains('required'))) && inputVazio && paragraphInput) {
                paragraph.style.display = 'block'
                input.style.outline = '1px solid #E50914'
                input.style.border = '1.5px solid transparent'
            }
        })
    }

    input.addEventListener('input', exibeAlertaInputs)
    input.addEventListener('blur', exibeAlertaInputs)
})

function verificaInput(id) {
    field = document.getElementById(id).value

    if (id == 'idade') {
        return Number(field) < 0 || Number(field) > 100
    }
    return field.length < 1
}

function validaInputs() {
    if (verificaInput("nome") || verificaInput("idade") || (verificaInput("outros-filmes") && checkboxes[4].checked)) {
        return false
    }
    else {    
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

buttonReset.addEventListener('click', () => {
    triangleIcon.style.display = 'none'
    badgeIcon.style.display = 'block'
    exibeModal("Formulário limpo com sucesso!")

    form.reset()

    paragraphs.forEach(paragraph => paragraph.style.display = 'none')
    inputs.forEach(input => input.style = 'border: 1.5px solid rgb(201, 201, 201); outline: none;')
})

buttonSubmit.addEventListener('click', (event) => {
    let checkboxesVazias = !checkboxes[0].checked && !checkboxes[1].checked && !checkboxes[2].checked && !checkboxes[3].checked && !checkboxes[4].checked,
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

        inputs.forEach(input => {
            paragraphs.forEach(paragraph => {
                if(input.id == 'outros-filmes' && paragraph.id == 'outros-filmes') {
                    input.setAttribute('class', 'required')
                    paragraph.style.display = 'block'
                }
            })
        })

    }
})