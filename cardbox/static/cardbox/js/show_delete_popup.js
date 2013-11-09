function show_delete_popup(path) {
    if ($("#card_delete_popup").is(':visible')) {
        return;
    }
    $("#card_delete_popup_form").get(0).setAttribute('action', path);
    $("#card_delete_popup").show()
}

function hide_delete_popup() {
    if ($("#card_delete_popup").is(':visible')) {
        $("#card_delete_popup_form").get(0).setAttribute('action', '#');
        $("#card_delete_popup").hide()
    }
}