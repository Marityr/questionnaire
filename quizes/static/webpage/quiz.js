const startTest = document.getElementById('body-form')

var global = 0

const sendData = () => {
    const elements = [...document.getElementById('body-form')]
    const data = {}

    elements.forEach(el => {
        if (el) {
            data[el.name] = el.value
        } else {
            if (!data[el.name]) {
                data[el.name] = null
            }
        }

        if (el.type == 'submit') {
            var step = Number($(el).attr('bstep'));
            var progress = Number($('.progress-bar').attr('aria-valuenow'));

            $('.step-' + step + '').removeClass('form-active');
            $('.step-' + (step + 1) + '').addClass('form-active');
            console.log(progress)
            $('.progress-bar').attr('style', 'width: ' + (progress + 5) + '%');
            $('.progress-bar').attr('aria-valuenow', (progress + 5));
            console.log(step)
        }
    })

    console.log(data)

    $.ajax({
        type: 'POST',
        url: `save/`,
        data: data,
        success: function (response) {
            console.log(response)
        },
        error: function (error) {
            console.log(error)
        },
    })
}









