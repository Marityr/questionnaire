console.log('hello world')

const headerBlock = document.getElementById('header-block')
const bodyBlock = document.getElementById('body-block')
const footerBlock = document.getElementById('footer-block')
const buttonBlock = document.getElementById('button-block')
const bodyForm = document.getElementById('body-form')
const bodyFormInput = document.getElementById('body-form-input')

const startQuiz = document.getElementById('activate-test')

const url = document.location.href


startQuiz.addEventListener('click', () => {
    bodyBlock.innerHTML = `
        <p>
        Для начала тестирования заполните форму ниже
        </p>
    `  
    bodyFormInput.innerHTML = `
    <input class="form-control form-control-lg" type="text" placeholder="Имя" name="name">
    <input class="form-control form-control-lg" type="email" placeholder="Email" name="email">
    <select class="form-select" aria-label="Default select example" name="male">
        <option selected>Gender</option>
        <option value="male">Male</option>
        <option value="famele">Femele</option>
        <option value="nonbinary">Non-binary</option>
        <option value="transgender">Transgender</option>
        <option value="intersex">Intersex</option>
        <option value="iprefernottosay">I prefer not to say</option>
        <option value="letmetype">Other</option>
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

    console.log(url)

    $.ajax({
        type: 'POST',
        url: ``,
        data: data,
        success: function (response) {
            uid = response
            console.log(response)
            window.location.replace(`${url}${uid['uid']}`);
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