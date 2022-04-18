const bodyBlock = document.getElementById('body-block')
const buttonBlock = document.getElementById('button-block')

const startQuiz = document.getElementById('activate-test')

const url = document.location.href


startQuiz.addEventListener('click', () => {
    console.log('1111');
    window.location.replace(`${url}accounts/login/`);
})
