$(document).ready(function() {
    console.log(question);

    let selectedChoice = "";
    let hasChecked = false;

    $('.next-btn').hide();

    $(".question-choice").click(function(){
        if (hasChecked)
            return;
        selectedChoice = $(this).data('id');
        console.log("selected:", selectedChoice)
        $(".selected-choice").removeClass('selected-choice');
        $(this).addClass('selected-choice');
    })

    $(".check-btn").click(function(){
        $(".question-alert-cont").empty();
        let alert_msg = "";
        if (selectedChoice === "") {
            alert_msg = `<div class="col-12 alert alert-warning" role="alert"> Please select an option from above!</div>`;
            $(".question-alert-cont").append(alert_msg);
            return;
        } 

        // finalSelectedChoice=selectedChoice;
        if (selectedChoice == question.answer_id)
            alert_msg = `<div class="col-12 alert alert-success" role="alert"> Correct!</div>`;
        else
            alert_msg = `<div class="col-12 alert alert-danger" role="alert"> Incorrect! The correct option is <span class="correct-explanation">${question.choices[parseInt(question.answer_id)]}.</span></div>`;
        console.log("Alert_msg:", alert_msg)

        $(".question-alert-cont").append(alert_msg);
        
        hasChecked = true;
        $('.question-choice').removeClass('hoverable');
        $('.next-btn').show();
        $('.check-btn').hide();
    })

    $(".next-btn").click(function(){
        window.location.href = `/quiz/log_response/${selectedChoice}`;
    })

})