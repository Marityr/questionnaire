console.log('hello world')

$(document).on('click', '#step', function(){
    var step = Number($(this).attr('bstep'));
    var step = Number($(this).attr('aria-valuenow'));
    
    $('.step-' + step + '').removeClass('form-active');
    $('.step-' + (step+1) + '').addClass('form-active');
    $('.progress-bar').attr('style', 'width: ' +  + '%');
});