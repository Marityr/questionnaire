console.log('hello world');

const modalBtns = [...document.getElementsByClassName('modal-button')]
const modalBody = document.getElementById('modal-body-confirm')
const startBtn = document.getElementById('start-button')

const url = window.location.href

modalBtns.forEach(modalBtn => modalBtn.addEventListener('click', () => {
    const pk = modalBtn.getAttribute('data-pk')
    const name = modalBtn.getAttribute('data-name')

    modalBody.innerHTML = `
        <div>Ваш уникальный ID в системе - 363463</div>
        <hr>
        <form action="">
            Укажите свой пол
            <select>
                <option value="----------" default>----------</option>
                <option value="Мужчина">Мужчина</option>
                <option value="Женщина">Женщина</option>
            </select>
        </form>
    `

    startBtn.addEventListener('click', () => {
       window.location.href = url + pk
    })
}))