// console.log('hello world')

// const url = window.location.href

// $(document).on('click', '#step', function () {
//     var step = Number($(this).attr('bstep'));
//     var progress = Number($('.progress-bar').attr('aria-valuenow'));

//     function foo() {
//         $('#bstep-'+step+'').click()
//         console.log(data)
//     }
//     setTimeout(foo, 1000);

//     // $.ajax({
//     //     method: "GET",
//     //     dataType: "json",
//     //     url: `${url}save`,
//     //     success: function () {
//     //         console.log('true')
//     //     }
//     // })

//     // const data = {}
//     // data['csrfmiddlewaretoken'] = csrf[0].value
//     // elements.forEach(el => {
//     //     if (el) {
//     //         data[el.name] = el.value
//     //     } else {
//     //         if (!data[el.name]) {
//     //             data[el.name] = null
//     //         }
//     //     }
//     // })

//     // $.ajax({
//     //     type: 'POST',
//     //     data: data,
//     //     url: `${url}save`,
//     //     success: function (response) {
//     //         $('.step-' + step + '').removeClass('form-active');
//     //         $('.step-' + (step + 1) + '').addClass('form-active');
//     //         console.log(progress)
//     //         $('.progress-bar').attr('style', 'width: ' + (progress + 10) + '%');
//     //         $('.progress-bar').attr('aria-valuenow', (progress + 10));
//     //         console.log(response)
//     //     },
//     //     error: function (error) {
//     //         confirm.log(error)
//     //     }
//     // })
//     // $('#import_all_button').on('click', function () {
//     //     $('.import_true').removeClass('animate_hiden')
//     //     $('.import').removeClass('animate_hiden')
//     //     $('.import_true').addClass('animate_hiden')
//     //     $.ajax({
//     //         method: "GET",
//     //         dataType: "json",
//     //         url: "{% url 'importxl_all' %}",
//     //         success: function () {
//     //             $('.import_true').removeClass('animate_hiden')
//     //             $('.import').addClass('animate_hiden')
//     //             console.log('true')
//     //         }
//     //     })
//     // })
// });

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
            // console.log(progress)
            $('.progress-bar').attr('style', 'width: ' + (progress + 10) + '%');
            $('.progress-bar').attr('aria-valuenow', (progress + 10));
            // console.log(step)
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

// startTest.addEventListener('submit', e => {
//     e.preventDefault()
//     sendData()
//     $(this).parent().html(data);
// })








