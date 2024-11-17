const datepicker = document.querySelector('.datepicker'),
datePickerContainer = document.querySelector('.datepicker-container'),
dateInput = document.querySelector('#data_nascimento'),
spanInput = document.querySelector('#msgError'),
iconCalendar = document.querySelector('.icon-calendar'),
yearInput = datepicker.querySelector('.year-input'),
monthInput = document.querySelector('.month-input'),
cancelButton = datepicker.querySelector('.cancel'),
saveButton = datepicker.querySelector('.apply'),
dates = datepicker.querySelector('.dates'),
nextButton = datepicker.querySelector('.next'),
prevButton = datepicker.querySelector('.prev'),
submitButton = document.querySelector('#submit'),
form = document.querySelector('form'),
select = document.querySelector('.select'),
selectedValue = document.getElementById('selected-value'),
inputsMonthOptions = document.querySelectorAll('.option input'),
optionsMonths = document.getElementById('month'),
telefoneInput = document.querySelector('#telefone');

let selectedDate = new Date();
let month = selectedDate.getMonth();
let year = selectedDate.getFullYear();

const monthsMap = {
    'Janeiro': 0,
    'Fevereiro': 1,
    'Março': 2,
    'Abril': 3,
    'Maio': 4,    
    'Junho': 5,
    'Julho': 6,
    'Agosto': 7,
    'Setembro': 8,
    'Outubro': 9,
    'Novembro': 10,
    'Dezembro': 11
};

lucide.createIcons();

dateInput.addEventListener('change', () => {
    const age = new Date().getFullYear() - dateInput.value.split('-')[0];
    if (dateInput.value.split('-')[0] < 1900 || dateInput.value.split('-')[0] >= 2024) {
        spanInput.hidden = false;
        spanInput.textContent = 'Data de nascimento inválida';
        dateInput.classList.add('error');
        return;
    }
    checkAge(age);
});

iconCalendar.addEventListener('click', () => {
    datepicker.classList.toggle('active');
});

nextButton.addEventListener('click', () => {
    if (year === 2024 & month === 11) return;
    if (month === 11) year++;
    month = (month + 1) % 12;

    displayDates();
});

prevButton.addEventListener('click', () => {
    if (year <= 1900 && month === 0) return;
    if (month === 0) year--;
    month = (month - 1 + 12) % 12;

    displayDates();
});

cancelButton.addEventListener('click', () => {
    datepicker.classList.remove('active');
});

saveButton.addEventListener('click', () => {    
    const formattedDate = selectedDate.toISOString().split('T')[0];
    const age = new Date().getFullYear() - formattedDate.split('-')[0];
    
    dateInput.type = 'date';
    dateInput.value = formattedDate;
    
    checkAge(age);
    iconCalendar.click();
});

inputsMonthOptions.forEach(input => {

    input.addEventListener('change', event => {
        const selectedMonth = input.dataset.label;

        selectedValue.textContent = selectedMonth;
        optionsMonths.removeAttribute('required');

        month = monthsMap[selectedMonth];

        updateYearMoth();
        displayDates();

        const isMouseOrTouch = event.pointerType == 'mouse' || event.pointerType == 'touch'
        
        !isMouseOrTouch && optionsMonths.click()
    })
})

yearInput.addEventListener('change', () => {
    if (yearInput.value < 1900 || yearInput.value >= 2024) yearInput.value = selectedDate.getFullYear();
    year = yearInput.value;

    updateYearMoth();
    displayDates();
});

submitButton.addEventListener('click', (e) => {

    if(dateInput.classList.contains('error')) {
        e.preventDefault();
        return;
    }

    form.submit();
    form.reset();

});

telefoneInput.addEventListener('input', () => {
    telefoneInput.value = telefoneInput.value.replace(/\D/g, '').replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
});

const checkAge = (age) => {
    if(age < 18) {
        spanInput.hidden = false;
        spanInput.textContent = 'Você deve ter pelo menos 18 anos para se cadastrar';
        dateInput.classList.add('error');
        return;
    } else {
        spanInput.hidden = true;
        dateInput.classList.remove('error');
    }
}

const updateYearMoth = () => {
    monthsMap[month] = month;
    selectedValue.textContent = inputsMonthOptions[month].dataset.label;
    inputsMonthOptions[month].checked = true;
    yearInput.value = year;
}

const handleDaySelected = (e) => {
    var selected = dates.querySelector('.selected');
    const button = e.target;

    selected && selected.classList.remove('selected');
    button.classList.add('selected');
    selectedDate = new Date(year, month, parseInt(button.textContent));
}

const displayDates = () => {
    let firstDayofMonth = new Date(year, month, 1).getDay(),
    lastDateofMonth = new Date(year, month + 1, 0).getDate(),
    lastDayofMonth = new Date(year, month, lastDateofMonth).getDay(),
    lastDateofLastMonth = new Date(year, month, 0).getDate();
    
    dates.innerHTML = '';

    updateYearMoth();
    
    for (let i = firstDayofMonth; i > 0; i--) {
        const text = lastDateofLastMonth - i + 1;
        const button = createButton(text, true, -1);
        dates.appendChild(button);
    }

    for (let i = 1; i <= lastDateofMonth; i++) {
        const button = createButton(i, false);

        button.addEventListener('click', handleDaySelected);
        dates.appendChild(button);
    }

    for (let i = lastDayofMonth; i < 6; i++) {
        const text = i - lastDayofMonth + 1;
        const button = createButton(text, true, 1);
        dates.appendChild(button);
    }
}

const createButton = (text, isDisabled = false, type = 0) => {
    let comparisionDate = new Date(year, month + type, text);

    const button = document.createElement('button'),
    currentDate = new Date(),
    selected = selectedDate.getTime() === comparisionDate.getTime(),
    isToday = 
    currentDate.getDate() === text && 
    currentDate.getMonth() === month && 
    currentDate.getFullYear() === year;

    button.setAttribute('type', 'button');
    button.textContent = text;
    button.disabled = isDisabled;
    button.classList.toggle('today', isToday && !isDisabled);
    button.classList.toggle('selected', selected);
    
    return button;
}


displayDates();