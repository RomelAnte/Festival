$(document).ready(function() {
    $("#fecha_nacimiento").on("input", function () {
        if ($(this).val() !== "") {
            $(this).css("color", "#000"); // Color negro si hay un valor
        } else {
            $(this).css("color", "transparent"); // Color transparente si está vacío
        }
    });

    $("#start_date").on("input", function () {
        if ($(this).val() !== "") {
            $(this).css("color", "#000"); // Color negro si hay un valor
        } else {
            $(this).css("color", "transparent"); // Color transparente si está vacío
        }
    });

    $("#end_date").on("input", function () {
        if ($(this).val() !== "") {
            $(this).css("color", "#000"); // Color negro si hay un valor
        } else {
            $(this).css("color", "transparent"); // Color transparente si está vacío
        }
    });
});