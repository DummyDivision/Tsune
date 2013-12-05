function show_answer() {
    if ($("#answer").is(':visible')) {
        return;
    }
    $("#answer").show()
    $("#rating").show()
    $("#preanswer").hide()
}

if ($.urlParam('showAnswer')=='true'){
    $(show_answer);
}