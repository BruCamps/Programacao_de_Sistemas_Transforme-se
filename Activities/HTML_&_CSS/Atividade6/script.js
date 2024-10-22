lucide.createIcons()

let inputs = document.querySelectorAll('form input[type="text"]'),
    textareas = document.querySelectorAll('form textarea'),
    paragraphs = document.querySelectorAll('form .alert-msg'),
    cep = document.getElementById('cep'),
    select = document.querySelector('.select'),
    selectedValue = document.getElementById('selected-value'),
    optionsEstado = document.getElementById('estado'),
    inputsOptions = document.querySelectorAll('.option input'),
    buttonReset = document.querySelector('button[type="reset"]'),
    buttonSubmit = document.querySelector('button[type="submit"]')

const form = document.getElementById('form'),
    Modalcontainer = document.getElementById('alert'),
    msgModal = document.getElementById('alert-message'),
    triangleIcon = document.getElementById('triangle-alert'),
    badgeIcon = document.getElementById('badge-check'),
    closeBtn = document.querySelector('.close-button'),
    confirmBtn = document.getElementById('alert-confirm')

cep.addEventListener('input', () => {
    if (cep.value.length == 5) {
        cep.value += '-' 
    }
})


function verificaInput(id) {
    var field = document.getElementById(id).value
    
    if (id == 'nome' || id == 'endereco' || id == 'cidade' || id == 'interesses') {
        return field.length < 3
    } 
    if (id == 'cep') {
        return field.length < 9
    }
}

function validaInputs() {
    if (
        verificaInput("nome") || 
        verificaInput("endereco") || 
        verificaInput("complemento") ||
        verificaInput("cidade") ||
        verificaInput("cep") ||
        verificaInput("interesses")
    ) {
        return false
    } else {    
        return true    
    }
}

inputs.forEach(input => {

    input.addEventListener('input', () => {

        paragraphs.forEach(paragraph => {

            inputVazia = input.value.length == 0
            totalCaracteres = input.value.length
            paragraphInput = paragraph.id == input.id

            if(paragraphInput && (totalCaracteres >= 3 || inputVazia) ) {
                paragraph.style.display = 'none'
                input.style.outline = 'none'
                input.style.border = '1.5px solid rgb(201, 201, 201)'
            }
            
            if ((input.id == 'nome') && (totalCaracteres < 3 && !inputVazia && paragraphInput) ||
                (input.id == 'cidade') && (totalCaracteres < 4 && !inputVazia && paragraphInput) ||
                (input.id == 'cep' || input.id == 'endereco') && (totalCaracteres < 9 && !inputVazia && paragraphInput)) {
                paragraph.style.display = 'block'
                input.style.outline = '1px solid #F23D91'
                input.style.border = '1.5px solid transparent'
            }
        })
    })
    
})

textareas.forEach(textarea => {

    textarea.addEventListener('input', () => {

        paragraphs.forEach(paragraph => {

            textareaVazia = textarea.value.length == 0
            totalCaracteres = textarea.value.length
            paragraphTextarea = paragraph.id == textarea.id

            if (paragraphTextarea && (totalCaracteres >= 5 || textareaVazia)) {
                paragraph.style.display = 'none'
                textarea.style.outline = 'none'
                textarea.style.border = '1.5px solid rgb(201, 201, 201)'
            }
            
            if (textarea.id == 'interesses' && (totalCaracteres < 5 && !textareaVazia && paragraphTextarea)) {
                paragraph.style.display = 'block'
                textarea.style.outline = '1px solid #F23D91'
                textarea.style.border = '1.5px solid transparent'
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

inputsOptions.forEach(input => {

    input.addEventListener('change', event => {
        selectedValue.textContent = input.dataset.label
        optionsEstado.removeAttribute('required', true)
        
        const isMouseOrTouch = event.pointerType == 'mouse' || event.pointerType == 'touch'
        
        !isMouseOrTouch && optionsEstado.click()
    })
})

buttonReset.addEventListener('click', () => {
    triangleIcon.style.display = 'none'
    badgeIcon.style.display = 'block'
    exibeModal("Formulário limpo com sucesso!")

    form.reset()

    selectedValue.textContent = 'Selecione um estado'
    optionsEstado.setAttribute('required', true)

    paragraphs.forEach(paragraph => paragraph.style.display = 'none')
    inputs.forEach(input => input.style = 'border: 1.5px solid rgb(201, 201, 201); outline: none;')
    textareas.forEach(textarea => textarea.style = 'border: 1.5px solid rgb(201, 201, 201); outline: none;')
})

buttonSubmit.addEventListener('click', (event) => {
    event.preventDefault()

    if (!validaInputs() || optionsEstado.hasAttribute('required')) {
        triangleIcon.style.display = 'block'
        badgeIcon.style.display = 'none'

        exibeModal('Todos os campos devem ser preenchidos!')
    }

    if (validaInputs() && !optionsEstado.hasAttribute('required')) {
        triangleIcon.style.display = 'none'
        badgeIcon.style.display = 'block'

        exibeModal('Simulação de cadastrado feita com sucesso!')

        selectedValue.textContent = 'Selecione um estado'
        optionsEstado.setAttribute('required', true)

        form.reset()
    }
})