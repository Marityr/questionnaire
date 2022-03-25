console.log('hello world')

const headerBlock = document.getElementById('header-block')
const bodyBlock = document.getElementById('body-block')
const footerBlock = document.getElementById('footer-block')
const buttonBlock = document.getElementById('button-block')
const bodyForm = document.getElementById('body-form')
const bodyFormInput = document.getElementById('body-form-input')

const startQuiz = document.getElementById('activate-test')


startQuiz.addEventListener('click', () => {
    bodyBlock.innerHTML = `
        <p>
        Для начала тестирования заполните форму ниже
        </p>
    `  
    bodyFormInput.innerHTML = `
    <input class="form-control form-control-lg" type="text" placeholder="Имя" name="name">
    <input class="form-control form-control-lg" type="email" placeholder="Email" name="emil">
    <select class="form-select" aria-label="Default select example" name="male">
        <option selected>Open this select menu</option>
        <option value="1">One</option>
        <option value="2">Two</option>
        <option value="3">Three</option>
    </select>
    <button type="submit" class="btn btn-lg w-100 btn-primary" name="button" id="step-1">Далее</button>
    `  
    buttonBlock.innerHTML = ``
})

const csrf = document.getElementsByName('csrfmiddlewaretoken')
const startTest = document.getElementById('body-form')

const sendData = () => {
    const elements = [...document.getElementById('body-form')]
    const data = {}
    data['csrfmiddlewaretoken'] = csrf[0].value
    elements.forEach(el => {
        if (el) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }
    })

    console.log(data)

    $.ajax({
        type: 'POST',
        url: `data`,
        data: data,
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        },
    })
}

startTest.addEventListener('submit', e => {
    e.preventDefault()
    
    sendData()
})