$(document).ready(function() {
    console.log(question);

    let selectedChoice = "";
    $('.next-btn').hide();

    $(".question-choice").click(function(){
        selectedChoice = $(this).data('id');
        $(".selected-choice").removeClass('selected-choice');
        $(this).addClass('selected-choice');
        $('.next-btn').show();
    })

    $(".next-btn").click(function(){
        window.location.href = `/quiz/log_response/${selectedChoice}`;
    })
})