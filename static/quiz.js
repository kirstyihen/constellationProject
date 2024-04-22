$(document).ready(function() {
    console.log(question);

    let selectedOption = "";

    $(".feature-box").click(function(){
        selectedOption = $(this).data('id');
        // console.log("selected:", selectedOption);
        $(".selected-option").removeClass('selected-option');
        $(this).addClass('selected-option');
    })

    $(".next-btn").click(function(){
        window.location.href = `/quiz/log_response/${selectedOption}`;
    })
})