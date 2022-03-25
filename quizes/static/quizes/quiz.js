console.log('hello world')

const url = window.location.href

const quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        const data = response.data
        console.log(data)
        quizBox.innerHTML += `
            <input type="text" class="ans" name="IDuser" value="3452543">
        `
        data.forEach(el => {
            for (const [question, answers] of Object.entries(el)) {
                quizBox.innerHTML += `
                    <hr>
                    <div class="mb-2">
                        <b>${question}</b>
                    </div>
                `
                answers.forEach(answer => {
                    quizBox.innerHTML += `
                        <div>
                            <input type="number" class="ans" id="${question}-${answer}" name="${answer[0]}" min="0" max="2" value="1" required>
                            <label for="${question}">${answer[1]}</label>
                        </div>
                    `
                })

                quizBox.innerHTML += `
                    <button type="button" class="btn btn-primmary mt-3">Далее</button>
                `
            }
        });
    },
    error: function (error) {
        console.log(error)
    }
})

const quizForm = document.getElementById('quiz-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const sendData = () => {
    const elements = [...document.getElementsByClassName('ans')]
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

    $.ajax({
        type: 'POST',
        url: `${url}save/`,
        data: data,
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        },
    })
}

quizForm.addEventListener('submit', e => {
    e.preventDefault()

    sendData()
})