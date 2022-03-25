console.log('hello world')

const headerBlock = document.getElementById('header-block')
const bodyBlock = document.getElementById('body-block')
const footerBlock = document.getElementById('footer-block')
const buttonBlock = document.getElementById('button-block')
const bodyForm = document.getElementById('body-form')
const bodyFormInput = document.getElementById('body-form-input')
const formesBlock = document.getElementById('formes')


const url = window.location.href

$.ajax({
    type: 'GET',
    url: `${url}data`,
    success: function (response) {
        let data = response.data
        // console.log(data)
        var step = 1;
        data.forEach(el => {
            formesBlock.innerHTML += `
                <form id="step" step="${step}">
                <div id="step-${step}"></div>
                
                <button type="button" class="step" bstep="${step}">${step}</button>
                <button type="submit" class="btn btn-lg w-100 btn-primary" name="button" id="btn-${step}">Далее</button>
                </form>
            `

            for (const [question, answers] of Object.entries(el)) {
                document.getElementById('step-'+ step ).innerHTML += `
                    <b>${question}</b><br>
                `
                answers.forEach(answer => {
                    document.getElementById('step-'+ step ).innerHTML += `
                        <div class="form-block-step">
                        <label for="${question}">${answer[1]}</label>
                        <input type="number" class="ans" id="${question}-${answer}" name="${answer[0]}" min="0" max="2" value="" autocomplete="off" required>
                        </div>
                        `
                })
            }
            step++;
        });

        const csrf = document.getElementsByName('csrfmiddlewaretoken')
        const stepButton = document.getElementById('step')

        stepButton.addEventListener('submit', e => {
            e.preventDefault()
            
            console.log(e)
        })
    },
    error: function (error) {
        console.log(error)
    }
})

$(document).on('click', '.step', function(){
    var step = $(this).attr('bstep')
    var btnid = '#btn-'  + step + ''

    $(btnid).trigger('click', function(){
        $.ajax({
            type: "POST",
            data: stepdata,
            url: `${url}save`,
            success: function (response) {
                console.log('try')
            },
            error: function(error){
                console.log('false')
            }

        })
    });
});