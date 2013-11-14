function show_delete_popup(path) {
    if ($("#delete_popup").is(':visible')) {
        return;
    }
    $("#delete_popup_form").get(0).setAttribute('action', path);
    $("#delete_popup").show()
}

function hide_delete_popup() {
    if ($("#delete_popup").is(':visible')) {
        $("#delete_popup_form").get(0).setAttribute('action', '#');
        $("#delete_popup").hide()
    }
}